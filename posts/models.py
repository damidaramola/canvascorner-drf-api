from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    """
    post model which relates to User instance 
    """
    category_choices = [
        ('novice', 'Novice'),
        ('intermediate', 'Intermediate'),
        ('professional', 'Professional')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=category_choices,
                                default='normal')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/',
                              default='../default_profile_vvucyn', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
