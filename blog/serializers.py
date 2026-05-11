from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Category, Post

class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'author', 'id', 'category_name', 'author_username']

    def get_category_name(self, obj):
        return obj.category.name

    def get_author_username(self, obj):
        return obj.author.username

class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'posts']

    def get_posts(self, obj):
        posts = obj.post_set.all()
        return PostSerializer(posts, many=True).data

class UserSerilizer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user