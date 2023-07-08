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

    """
    Test to make sure a logged out in user can't create a post
    make test fail by adding 201 status code instead of 403 forbidden code
    status
    """

    def test_logged_out_user_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    """
    set up unit tests for post detail
    """


class PostDetailViewTests(APITestCase):
    def setUp(self):
        dami = User.objects.create_user(username='dami', password='passw')
        anna = User.objects.create_user(username='anna', password='passw')
        Post.objects.create(
            owner=dami, title='title', description='damis content'
        )
        Post.objects.create(
            owner=anna, title='second title', description='annas content'
        )

    """
    test if its possible to retrieve a post with a valid id 
    make test fail by using 201 status code instead of 200 status code
    """

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    test if its not possible to fetch a post with an invalid id 
    make test fail by using 200 status code instead of 404 status code
    """

    def test_cannot_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/13/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    test if a user can update their own posts
    make test fail by using 201 status code instead of 200 status code
    """

    def test_user_can_update_own_post(self):
        self.client.login(username='dami', password='passw')
        response = self.client.put('/posts/1/', {'title': 'title1'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'title1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
