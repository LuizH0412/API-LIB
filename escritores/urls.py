from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escritores import views

route = DefaultRouter()
route.register('escritores', views.EscritorViewSet, basename='escritores')

urlpatterns = [
    path('', include(route.urls))
]