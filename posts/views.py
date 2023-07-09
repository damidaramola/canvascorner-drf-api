from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from canvascorner_drf_api.permissions import IsOwnerOrReadOnly

# Create PostList View


class PostList(generics.ListCreateAPIView):
    """
    Make sure users are authenticated and logged in when requesting
    write access
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
