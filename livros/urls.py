from rest_framework.routers import DefaultRouter
from django.urls import path, include
from livros import views

route = DefaultRouter()
route.register('livros', views.LivroViewSet, basename='livros')

urlpatterns = [
    path('', include(route.urls))
]