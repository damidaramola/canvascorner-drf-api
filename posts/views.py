from django.http import Http404
from rest_framework import status, permissions
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from canvascorner_drf_api.permissions import IsOwnerOrReadOnly

# Create PostList View


class PostList(APIView):
    serializer_class = PostSerializer
    """
    Make sure users are authenticated when requesting
    write access
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={
            'request': request
        })
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer

    def get_object(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    """
    get method allows you to retrieve the post by ID
    """

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, context={'request': request})
        return Response(serializer.data)

    # def get(self, request, pk):
    #     post = self.get_object(pk)
    #     serializer = PostSerializer(
    #         post, data=request.data, context={'request': request})
    #     return Response(serializer.data)
   