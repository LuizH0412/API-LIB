from rest_framework.routers import DefaultRouter
from emprestimos import views
from django.urls import path, include

route = DefaultRouter()
route.register('emprestimos', views.EmprestimoViewSet, basename='emprestimos')

urlpatterns = [
    path('', include(route.urls))
]