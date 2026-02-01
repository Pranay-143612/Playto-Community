from django.urls import path
from .views import PostListCreateAPIView, CommentListCreateAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
]
