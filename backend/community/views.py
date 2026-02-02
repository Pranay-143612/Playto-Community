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
from django.contrib.auth.models import User
from rest_framework import status

class EmailLoginAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")

        if not email:
            return Response(
                {"error": "Email is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user, created = User.objects.get_or_create(
            username=email,
            defaults={"email": email}
        )

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created": created
        })

# ----------------- Posts -----------------
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.select_related('author').prefetch_related(
        'comments', 'comments__replies'
    ).all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# ----------------- Comments -----------------
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.select_related('author', 'post').prefetch_related('replies').all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

# ----------------- Likes -----------------
class LikeCreateAPIView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

# ----------------- Leaderboard -----------------
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



