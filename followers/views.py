from rest_framework import generics, permissions
from canvascorner_drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

"""
       A class for FollowerList all instances of a user can be listed 
       'create' a follow where logged in users can follow another account 
       Perform_create associates the current logged in user with a follower.
       """


class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    """
    A class for FollowerDetail
    User to be able to retrieve and delete their follow
    """


class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
