from rest_framework import status, permissions
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer

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
        serializer = PostSerializer(data=request, context={'request': request})
        if serializer.isvalid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
