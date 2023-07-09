from django.db import models
from django.contrib.auth.models import User

""" 
Create follower model which has a foreignkey relationship with 
User model
 the 'owner' is a User that is following another User
 the related_name attribute differentiates between the owner and 
 followed which are both instances of the user model
"""


class Follower(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='followed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
