from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from blog.views import home, category_list, category_create, category_detail_update, category_detail_delete
from blog.viewsets import CategoryViewSet, PostViewSet

router = DefaultRouter()
router.register(r'categories_router',
                CategoryViewSet,
                basename='categories')
router.register(r'posts_router',
                PostViewSet,
                basename='posts')
urlpatterns = [
    path('categories/',
         category_list,
         name='category_list'),
    path('categorie/create/',
         category_create,
         name='category_detail'),
    path('categories/<int:pk>/update/',
         category_detail_update,
         name='category_detail_update'),
    path('categories/<int:pk>/delete/',
         category_detail_delete,
         name='category_detail_delete'),
    path('auth/', obtain_auth_token),
] + router.urls