from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from canvascorner_drf_api.permissions import IsOwnerOrReadOnly

"""
    add profile serializer to ProfileList
    ProfileList will list all profiles
    """


class ProfileList(generics.ListAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    """
    Retrieve or update a profile if you're the owner.
    """


class ProfileDetail(generics.RetrieveUpdateAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
