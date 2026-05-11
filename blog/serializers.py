from rest_framework import serializers

from blog.models import Category, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'author', 'id']

class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'posts']

    def get_posts(self, obj):
        posts = obj.post_set.all()
        return PostSerializer(posts, many=True).data