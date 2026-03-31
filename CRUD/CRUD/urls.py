from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),

    # Rutas de autenticación (usuarios)
    path('api/auth/', include('usuario.urls')),

    # Rutas de negocios (tu otra app)
    path('api/', include('negocio.urls')),
]