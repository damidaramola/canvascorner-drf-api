from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    """
    Automatically runs before every test method
    """

    def setUp(self):
        User.objects.create_user(username='dami', password='passw')
    """
    Test to make a get request to /posts/ to list all posts
    make test fail by adding 201 status instead of 200 status
    """

    def test_can_list_posts(self):
        dami = User.objects.get(username='dami')
        Post.objects.create(owner=dami, title='title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    """
    Test to make sure a logged in user can create a post
    make test fail by adding 200 status instead of 201 status
    """

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='dami', password='passw')
        response = self.client.post('/posts/', {'title': 'title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
