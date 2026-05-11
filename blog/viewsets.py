from logging import raiseExceptions

from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny

from blog.models import Category, Post
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import CategorySerializer, PostSerializer, UserSerilizer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        print("perform_create")
        print(self.request.user)
        if self.request.user.is_anonymous:
            raise Http404("Login first.")
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if self.request.user.is_anonymous:
            raise Http404("Login first.")
        if self.request.user != serializer.instance.author:
            raise Http404("You are not the author.")
        if self.request.user.is_superuser:
            serializer.save(author=self.request.user)
        serializer.save(author=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerilizer

