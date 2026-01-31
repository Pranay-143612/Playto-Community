from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} by {self.author.username}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.id} by {self.author.username}"


class Like(models.Model):
    POST = 'post'
    COMMENT = 'comment'

    TARGET_CHOICES = [
        (POST, 'Post'),
        (COMMENT, 'Comment'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_type = models.CharField(max_length=10, choices=TARGET_CHOICES)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'target_type', 'post', 'comment'],
                name='unique_like'
            )
        ]

    def __str__(self):
        return f"{self.user.username} liked {self.target_type}"
    def clean(self):
        if not self.post and not self.comment:
            raise ValidationError('Like must be for a post or a comment.')
