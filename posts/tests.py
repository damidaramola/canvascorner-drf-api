from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    """
    Automatically runs before every test method
    """

    def setUp(self):
        User.objects.create_User(username='dami', password='passw')
    """
    Test to make a get request to /posts/ to list all posts
    make test fail by adding 201 status instead of 200 status
    """    
    def test_can_list_posts(self):
        dami = User.objects.get(username='dami')
        Post.objects.create(owner=dami, title='title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)