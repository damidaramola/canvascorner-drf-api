from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
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
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    
    """
    Return posts of users posts that profile owner follows
    Return all the posts a user with a given profile id liked
    Return all the posts a user with a given profile id booked marked
    Return all user posts
    """
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'post_bookmarks__owner__profile',
        'owner__profile'
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


"""
if you own a post, get it ,edit it or delete it 
"""


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_at')
