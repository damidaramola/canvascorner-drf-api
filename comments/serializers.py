from rest_framework import serializers
from .models import Comment


""" 
create serializer for comments 
"""


class CommentSerializer(serializer.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'is_owner', 'profile_id', 'profile_image',
                  'created_at', 'updated_at', 'image', 'content']


class CommentDetailSerializer(CommentSerializer):
    """
    CommentDetailSerializer class
     inherits from the CommentSerializer
    """
    post = serializers.ReadOnlyField(source='post.id')
