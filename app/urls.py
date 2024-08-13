from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('generos.urls')),
    path('api/v1/', include('escritores.urls')),
    path('api/v1/', include('livros.urls')),
    path('api/v1/', include('usuarios.urls')),
    path('api/v1/', include('emprestimos.urls')),
    path('api/v1/', include('authentication.urls'))
]
