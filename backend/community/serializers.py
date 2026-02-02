from rest_framework import serializers
from .models import Post, Comment, Like, KarmaTransaction
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.exceptions import ValidationError

# ----------------- User -----------------
# serializers.py


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email']

    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['email'])
        user.save()
        return user


# ----------------- Post -----------------
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

# ----------------- Comment -----------------
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'parent', 'content', 'created_at', 'replies']

    def get_replies(self, obj):
        qs = obj.replies.all()
        serializer = CommentSerializer(qs, many=True)
        return serializer.data

    def create(self, validated_data):
        user = self.context['request'].user
        return Comment.objects.create(author=user, **validated_data)

# ----------------- Like -----------------
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'comment']

    def validate(self, data):
        if not data.get('post') and not data.get('comment'):
            raise ValidationError("Like must be for a post or a comment")
        return data

    def create(self, validated_data):
        user = self.context['request'].user

        with transaction.atomic():
            # Prevent double-like
            like, created = Like.objects.get_or_create(user=user, **validated_data)
            if not created:
                raise ValidationError("You have already liked this post/comment.")

            # Karma logic
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
