from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth.models import User

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




