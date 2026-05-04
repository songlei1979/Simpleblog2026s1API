from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Category
from blog.serializers import CategorySerializer


# Create your views here.

def home(request):
    #categories = CategorySerializer(Category.objects.all(), many=True).data
    category = Category.objects.first()
    category_serializer = CategorySerializer(category)
    return JsonResponse(category_serializer.data)


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def category_detail_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    if serializer.update(category, request.data):
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def category_detail_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return Response(status=204)
