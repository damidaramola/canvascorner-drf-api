from rest_framework import generics, permissions
from canvascorner_drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Likes
from like.serializers import LikesSerializer


class LikesList(generic.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
