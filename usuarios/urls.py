from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios import views

route = DefaultRouter()
route.register('usuarios', views.UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(route.urls))
]