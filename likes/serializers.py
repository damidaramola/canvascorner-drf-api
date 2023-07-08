from rest_framework import serializers
from .models import Likes
from django.db import IntegrityError

"""Create Likes Serializer
"""


class LikesSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Likes
        fields = ['id',
                  'owner',
                  'created_at',
                  'post',]

    """
    Handle if likes are duplicated by the same user 
    """

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication of like'
            })
