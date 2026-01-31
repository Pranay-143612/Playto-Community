from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(APIView):
    def get(self, request):
        # Efficient query: fetch author in same query
        posts = Post.objects.select_related('author').all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

