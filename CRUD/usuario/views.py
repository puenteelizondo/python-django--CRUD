from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UsuarioSerializer

# Obtener modelo de usuario configurado en settings
User = get_user_model()

# Vista para registrar usuarios
class RegistroView(generics.CreateAPIView):
    queryset = User.objects.all()  # Query base (requerido por DRF)
    serializer_class = UsuarioSerializer  # Serializer que usamos
    
    # Permite acceso sin autenticación (registro público)
    permission_classes = [permissions.AllowAny]