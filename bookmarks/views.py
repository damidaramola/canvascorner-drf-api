from rest_framework import generics, permissions
from canvascorner_drf_api.permissions import IsOwnerOrReadOnly
from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer

"""
    A class for BookmarkDetail
    User to be able to list and create their bookmark
    """


class BookmarkList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.object.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


"""
A class for BookmarkDetail
User to be able to retrieve and remove their bookmark 
"""


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
