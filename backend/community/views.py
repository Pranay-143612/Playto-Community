from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# List & Create posts
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.select_related('author').all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# List & Create comments
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.select_related('author', 'post').prefetch_related('replies').all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
