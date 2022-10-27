from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from users.models import User
# Create your models here.

app_name = 'contents'

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_authors = models.ManyToManyField(User, related_name='like_posts')


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)