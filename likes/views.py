from rest_framework import generics, permissions
from canvascorner_drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Likes
from likes.serializers import LikesSerializer


class LikesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    """
    A class for LikeDetail
    User to be able to retrieve and delete their like
    """


class LikesDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikesDetailSerializer
    queryset = Likes.objects.all()
