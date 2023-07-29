from rest_framework import serializers
from .models import Follower
from django.db import IntegrityError

"""Create Follower Serializer
"""


class FollowerSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id',
                  'owner',
                  'created_at',
                  'followed',
                  'followed_name',]

    """
    Handle if follow are duplication/integrity errors
    """
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication of follow'
            })