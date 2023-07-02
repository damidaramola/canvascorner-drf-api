from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

"""
profile model class
has a one-to-one relationship with user model
"""


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/',
                              default='../default_profile_vvucyn')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ['created_at']  


"""
Returns information on who the profile owner is
"""


def __str__(self):
    return f"{self.owner}'s profile"


"""
Trigger django signal when user creates a profile
"""


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)