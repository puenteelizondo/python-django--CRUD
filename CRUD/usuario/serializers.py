from rest_framework import serializers
from django.contrib.auth import get_user_model

# Obtiene el modelo activo de usuario (evita hardcodear)
User = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Modelo que vamos a serializar
        fields = ['id', 'username', 'email', 'password']  # Campos permitidos
        
        # Hace que el password no se devuelva en respuestas
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # create_user maneja el hash de contraseña correctamente
        user = User.objects.create_user(**validated_data)
        return user