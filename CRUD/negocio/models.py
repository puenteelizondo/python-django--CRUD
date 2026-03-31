from django.db import models
from django.contrib.auth import get_user_model
 
# Obtén el modelo User actual
User = get_user_model()
 
 
class Categoria(models.Model):
    """
    Categorías disponibles: Deportes, Cosméticos, etc
    
    Tablas en BD:
    - id (automático)
    - nombre
    """
    nombre = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = 'categorias'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.nombre
 
 
class Tienda(models.Model):
    """
    Tienda creada por un usuario autenticado
    
    Tablas en BD:
    - id (automático)
    - usuario_id (FK al usuario que la creó)
    - nombre
    - categoria_id (FK a la categoría)
    - sitio_web
    - fecha_creacion
    - activa
    """
    
    # ✅ RELACIÓN 1: Quién creó la tienda
    # Un usuario puede tener muchas tiendas
    # Si el usuario se elimina, se eliminan sus tiendas (CASCADE)
    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='tiendas'  # Permite user.tiendas.all()
    )
    
    # ✅ CAMPO 1: Nombre de la tienda (requerido, máx 150 caracteres)
    nombre = models.CharField(max_length=150)
    
    # ✅ RELACIÓN 2: A qué categoría pertenece
    # Una categoría tiene muchas tiendas
    # Si se elimina la categoría, error PROTECT (protege datos)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='tiendas'  # Permite categoria.tiendas.all()
    )
    
    # ✅ CAMPO 2: Sitio web (opcional, valida URL automáticamente)
    sitio_web = models.URLField(blank=True, null=True)
    
    # ✅ CAMPO AUTOMÁTICO: Fecha de creación (se llena solo al crear)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # ✅ CAMPO: Estado de la tienda (activa o no)
    activa = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'tiendas'
        # Constraint: Un usuario NO puede tener dos tiendas con el mismo nombre
        unique_together = ('usuario', 'nombre')
    
    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"