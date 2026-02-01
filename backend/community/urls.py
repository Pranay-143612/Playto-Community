from django.urls import path
from .views import (
    PostListCreateAPIView,
    CommentListCreateAPIView,
    LikeCreateAPIView,
    LeaderboardView
)

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('comments/', CommentListCreateAPIView.as_view()),
    path('like/', LikeCreateAPIView.as_view()),
    path('leaderboard/', LeaderboardView.as_view()),
]
