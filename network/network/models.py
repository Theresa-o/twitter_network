from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class User(AbstractUser):
    follows = models.ManyToManyField(
        "self", blank=True, related_name="fans", symmetrical=False
    )

    def __str__(self):
        return str(self.username)
    
class NewTweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post", blank=True, null=True,)

    def __str__(self):
        return f"{self.user} posted {self.caption}"

    class Meta: 
        # Orders posts by most recent first, by default
        ordering = ['-created_at']


class Profile(models.Model):
    user_before = models.OneToOneField(User, on_delete=models.CASCADE, related_name="author_before", null=True)
    follows_before = models.ManyToManyField(
        User, blank=True, related_name="followed_by_before", symmetrical=False
    )

    def __str__(self):
        return str(self.follows_before)
