"""
negocio/serializers.py

Convierte datos Python ↔ JSON y valida
"""

from rest_framework import serializers
from .models import Tienda, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    """Serializer para LISTAR categorías"""
    
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']
        read_only_fields = ['id']


class TiendaCrearSerializer(serializers.ModelSerializer):
    """Serializer para CREAR tiendas (formulario simplificado)"""
    
    class Meta:
        model = Tienda
        fields = ['nombre', 'categoria', 'sitio_web']
    
    def create(self, validated_data):
        """Automáticamente asigna el usuario del token"""
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)


class TiendaSerializer(serializers.ModelSerializer):
    """Serializer para LISTAR y VER tiendas (datos completos)"""
    
    usuario_username = serializers.CharField(
        source='usuario.username',
        read_only=True
    )
    
    categoria_nombre = serializers.CharField(
        source='categoria.nombre',
        read_only=True
    )
    
    class Meta:
        model = Tienda
        fields = [
            'id',
            'nombre',
            'categoria',
            'categoria_nombre',
            'sitio_web',
            'usuario_username',
            'fecha_creacion',
            'activa',
        ]
        read_only_fields = ['id', 'usuario_username', 'categoria_nombre', 'fecha_creacion']