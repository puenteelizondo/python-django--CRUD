from django.db import models
from django.contrib.auth.models import AbstractUser

# Heredamos de AbstractUser para NO reinventar autenticación
class Usuario(AbstractUser):
    # Campo automático: se llena al crear el usuario
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Campo automático: se actualiza cada vez que guardas cambios
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        # Nombre personalizado de la tabla en la base de datos
        db_table = 'usuarios'