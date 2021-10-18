from rest_framework import serializers

from .models import User, Post, PostLike

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('__all__')

class GetUserSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField(read_only=True)

    def get_posts(self, user):
        return user.posts.count()

    class Meta:
        model = User
        fields = ('username' , 'posts')

class GetPostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    author = serializers.SerializerMethodField(read_only=True)

    def get_likes(self, post):
        return post.liked_by.count()

    def get_author(self, post):
            return post.user.username

    class Meta:
        model = Post
        fields = ( 'id','body', 'author', 'likes')