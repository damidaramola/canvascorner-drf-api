from rest_framework import serializers
from .models import Bookmark
from django.db import IntegrityError

"""
Create Bookmark Serializer
"""


class BookmarkSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bookmark
        fields = ['id',
                  'owner',
                  'bookmarked_at',
                  'post', ]

    """
    Handle if bookmark is duplicated by the same user 
    """

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication of bookmark'
            })
