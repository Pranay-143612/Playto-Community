from rest_framework import serializers
from .models import Post, Comment, Like, KarmaTransaction
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


#post serilizer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'like_count', 'comment_count']

    def get_like_count(self, obj):
        return obj.like_set.filter(target_type='post').count()

    def get_comment_count(self, obj):
        return obj.comments.count()
    def create(self, validated_data):
        user = self.context['request'].user
        return Post.objects.create(author=user, **validated_data)

#comment serializers

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'parent', 'content', 'created_at', 'replies']

    def get_replies(self, obj):
        # recursive serialization for nested comments
        qs = obj.replies.all()
        serializer = CommentSerializer(qs, many=True)
        return serializer.data

    def create(self, validated_data):
        user = self.context['request'].user
        return Comment.objects.create(author=user, **validated_data)
    


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'comment']

    def validate(self, data):
        if not data.get('post') and not data.get('comment'):
            raise serializers.ValidationError(
                "Like must be for a post or a comment"
            )
        return data

    def create(self, validated_data):
        user = self.context['request'].user

        with transaction.atomic():
            like = Like.objects.create(user=user, **validated_data)

            # ✅ Karma logic
            if like.post:
                KarmaTransaction.objects.create(
                    user=like.post.author,
                    points=5,
                    post=like.post
                )
            elif like.comment:
                KarmaTransaction.objects.create(
                    user=like.comment.author,
                    points=1,
                    comment=like.comment
                )

        return like
