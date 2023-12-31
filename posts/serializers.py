from rest_framework import serializers
from posts.models import Post
from likes.models import Likes
from bookmarks.models import Bookmark

"""
create serializer for posts
"""


class PostSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    bookmark_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is larger that 2MB'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096 px'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096 px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    """
    check if the user is authenticated
    filter so that logged in user is the user
    who liked/bookmarked the post
    """

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Likes.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_bookmark_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=user, post=obj
            ).first()
            return bookmark.id if bookmark else None
        return None
    
    class Meta:
        model = Post
        fields = ['id', 'owner', 'is_owner', 'profile_id', 'profile_image',
                  'created_at', 'updated_at', 'like_id', 'bookmark_id',
                  'title', 'description', 'category', 'image',
                  'comments_count', 'likes_count',

                  ]
