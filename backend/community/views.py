from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Post, Comment, Like, KarmaTransaction
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.generics import CreateAPIView
from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta
from rest_framework.views import APIView
from rest_framework.response import Response


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

class LikeCreateAPIView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

class LeaderboardView(APIView):
    def get(self, request):
        last_24_hours = timezone.now() - timedelta(hours=24)

        leaderboard = (
            KarmaTransaction.objects
            .filter(created_at__gte=last_24_hours)
            .values('user__id', 'user__username')
            .annotate(total_karma=Sum('points'))
            .order_by('-total_karma')[:5]
        )

        return Response(leaderboard)

