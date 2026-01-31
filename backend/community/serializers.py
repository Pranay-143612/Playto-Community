from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

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
