"""

Conecta URLs a las vistas (rutas HTTP)
"""

from django.urls import path
from .views import (
    CategoriaListView,
    TiendaCreateView,
    TiendaListView,
    MisTiendasView,
    TiendaDetailView,
    TiendaPorCategoriaView,
    CategoriaCreateView,
)

urlpatterns = [
    # =========================================================================
    # CATEGORÍAS
    path('categorias/crear/', CategoriaCreateView.as_view(), name='categorias-crear'),
    # =========================================================================
    
    # GET /api/negocio/categorias/
    # Lista todas las categorías disponibles (sin token)
    path('categorias/', CategoriaListView.as_view(), name='categorias-list'),
    
    
    # =========================================================================
    # TIENDAS
    # =========================================================================
    
    # GET /api/negocio/tiendas/
    # Lista todas las tiendas activas del sistema (sin token)
    path('tiendas/', TiendaListView.as_view(), name='tiendas-list'),
    
    
    # POST /api/negocio/tiendas/crear/
    # Crear una tienda nueva (REQUIERE TOKEN)
    path('tiendas/crear/', TiendaCreateView.as_view(), name='tiendas-crear'),
    
    
    # GET /api/negocio/tiendas/{id}/
    # PUT /api/negocio/tiendas/{id}/
    # PATCH /api/negocio/tiendas/{id}/
    # DELETE /api/negocio/tiendas/{id}/
    # Ver, editar o eliminar UNA tienda (REQUIERE TOKEN y SER PROPIETARIO)
    path('tiendas/<int:pk>/', TiendaDetailView.as_view(), name='tiendas-detail'),
    
    
    # GET /api/negocio/tiendas/categoria/{categoria_id}/
    # Lista tiendas de una categoría específica (sin token)
    path('tiendas/categoria/<int:categoria_id>/', TiendaPorCategoriaView.as_view(), name='tiendas-por-categoria'),
    
    
    # =========================================================================
    # MIS TIENDAS (del usuario autenticado)
    # =========================================================================
    
    # GET /api/negocio/mis-tiendas/
    # Lista SOLO las tiendas del usuario autenticado (REQUIERE TOKEN)
    path('mis-tiendas/', MisTiendasView.as_view(), name='mis-tiendas'),
]