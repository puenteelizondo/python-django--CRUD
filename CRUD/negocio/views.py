
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Tienda, Categoria
from .serializers import TiendaSerializer, TiendaCrearSerializer, CategoriaSerializer


# ============================================================================
# VISTAS PARA CATEGORÍAS
# ============================================================================

class CategoriaListView(generics.ListAPIView):
    """
    GET /api/negocio/categorias/
    
    Lista todas las categorías disponibles
     SIN necesidad de token (AllowAny)
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.AllowAny]  # Cualquiera puede ver


# ============================================================================
# VISTAS PARA TIENDAS
# ============================================================================

class TiendaCreateView(generics.CreateAPIView):
    """
    POST /api/negocio/tiendas/crear/
    
    Crea una tienda nueva
     REQUIERE token JWT en header: Authorization: Bearer <token>
    
    Body esperado:
    {
        "nombre": "Mi Tienda de Deportes",
        "categoria": 1,
        "sitio_web": "https://motienda.com"
    }
    
    Respuesta:
    {
        "mensaje": "Tienda creada exitosamente ",
        "tienda": { ... datos de la tienda ... }
    }
    """
    serializer_class = TiendaCrearSerializer
    permission_classes = [permissions.IsAuthenticated]  #  REQUIERE TOKEN
    
    def perform_create(self, serializer):
        """
        Llamado después de validar el serializer
        Automáticamente asigna el usuario del token
        """
        serializer.save(usuario=self.request.user)
    
    def create(self, request, *args, **kwargs):
        """
        Sobrescribe el método create para personalizar la respuesta
        """
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                'mensaje': 'Tienda creada exitosamente ',
                'tienda': response.data
            },
            status=status.HTTP_201_CREATED
        )


class TiendaListView(generics.ListAPIView):
    """
    GET /api/negocio/tiendas/
    
    Lista TODAS las tiendas activas del sistema
     SIN necesidad de token (cualquiera puede ver)
    
    Respuesta:
    [
        { "id": 1, "nombre": "Tienda 1", ... },
        { "id": 2, "nombre": "Tienda 2", ... },
        ...
    ]
    """
    queryset = Tienda.objects.filter(activa=True)  # Solo tiendas activas
    serializer_class = TiendaSerializer
    permission_classes = [permissions.AllowAny]  # Cualquiera puede ver


class MisTiendasView(generics.ListAPIView):
    """
    GET /api/negocio/mis-tiendas/
    
    Lista SOLO las tiendas del usuario autenticado
     REQUIERE token JWT en header: Authorization: Bearer <token>
    
    Respuesta:
    [
        { "id": 1, "nombre": "Mi Tienda 1", ... },
        { "id": 2, "nombre": "Mi Tienda 2", ... },
        ...
    ]
    
    Si otro usuario hace request con su token, solo ve sus tiendas
    """
    serializer_class = TiendaSerializer
    permission_classes = [permissions.IsAuthenticated]  #  REQUIERE TOKEN
    
    def get_queryset(self):
        """
        Filtra automáticamente solo las tiendas del usuario autenticado
        self.request.user = usuario del token JWT
        """
        return Tienda.objects.filter(usuario=self.request.user)


class TiendaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/negocio/tiendas/{id}/
    PUT /api/negocio/tiendas/{id}/
    PATCH /api/negocio/tiendas/{id}/
    DELETE /api/negocio/tiendas/{id}/
    
    Ver, editar completo, editar parcial o eliminar UNA tienda
     REQUIERE token JWT y SER EL PROPIETARIO
    
    GET Respuesta:
    {
        "id": 1,
        "nombre": "Mi Tienda",
        "categoria": 1,
        "categoria_nombre": "Deportes",
        "sitio_web": "https://...",
        ...
    }
    
    PUT/PATCH Body:
    {
        "nombre": "Nuevo nombre",
        "categoria": 2,
        "sitio_web": "https://nuevo.com"
    }
    """
    serializer_class = TiendaSerializer
    permission_classes = [permissions.IsAuthenticated]  #  REQUIERE TOKEN
    queryset = Tienda.objects.all()
    
    def get_queryset(self):
        """
        Filtra solo las tiendas del usuario autenticado
        Impide que usuario1 edite tiendas de usuario2
        """
        return Tienda.objects.filter(usuario=self.request.user)
    
    def perform_update(self, serializer):
        """
        Asegura que el usuario no pueda cambiar el propietario
        """
        serializer.save(usuario=self.request.user)


class TiendaPorCategoriaView(generics.ListAPIView):
    """
    GET /api/negocio/tiendas/categoria/{categoria_id}/
    
    Lista tiendas de una categoría específica
     SIN necesidad de token
    
    Ejemplo: GET /api/negocio/tiendas/categoria/1/
    Respuesta: Lista de todas las tiendas activas de Deportes
    """
    serializer_class = TiendaSerializer
    permission_classes = [permissions.AllowAny]  # Cualquiera puede ver
    
    def get_queryset(self):
        """
        Obtén el categoria_id de la URL
        Filtra tiendas por esa categoría
        """
        categoria_id = self.kwargs.get('categoria_id')
        return Tienda.objects.filter(categoria_id=categoria_id, activa=True)


class CategoriaCreateView(generics.CreateAPIView):
    """POST /api/negocio/categorias/crear/"""
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.AllowAny]  # Temporal