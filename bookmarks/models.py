from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

"""
create model for user to save liked post in bookmarks 
"""


class Bookmark(models.Model):
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_bookmarks',
                             on_delete=models.CASCADE)
    bookmarked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-bookmarked_at']
        unique_together = ['owner', 'post']

        def __str__(self):
            return f'{self.owner} bookmarked {self.post}'
