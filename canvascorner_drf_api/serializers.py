from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

""" 
add the profile_id and profile_image to fields returned when  
requesting logged in user’s details.
"""


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
