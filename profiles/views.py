from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializers import ProfileSerializer
from canvascorner_drf_api.permissions import IsOwnerOrReadOnly

"""
    add profile serializer to ProfileList
    ProfileList will list all profiles
    use annotate method to add count fields to queryset
    avoid duplication using distinct=True
    """


class ProfileList(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count'
    ]

    """
    Allows you to Retrieve or update a profile if you're the owner.
    """


class ProfileDetail(generics.RetrieveUpdateAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
