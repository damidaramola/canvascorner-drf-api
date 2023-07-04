from rest_framework import serializers
from .models import Post

"""
create serializer for posts
"""


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField('owner.id')
    profile_image = serializers.ReadOnlyField('owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = ['id', 'owner', 'created_at', 'updated_at',
                  'title', 'description', 'image', 'is_owner']
