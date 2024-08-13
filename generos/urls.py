from django.urls import path, include
from rest_framework.routers import DefaultRouter
from generos import views

route = DefaultRouter()
route.register('generos', views.GeneroViewSet, basename='generos')

urlpatterns= [
    path('', include(route.urls))
]