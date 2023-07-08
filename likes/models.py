from django.db import models
from django.contrib.auth.model import User
from posts.models import Post

""" 
There is a relationship between user and Likes and posts
"""


class Likes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes',
                             on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(add_auto_now=True)

    class Meta:
        ordering = [-created_at]
        unique_together = ['owner', 'post']
        
        def __str__(self):
            return f'{self.owner} {self.post}'
