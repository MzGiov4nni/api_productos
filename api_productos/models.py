from django.db import models

# Create your models here.
class producto(models.Model):
    Nombre_Producto= models.CharField(max_length=100)
    Cantidad=models.PositiveSmallIntegerField()
    Precio=models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'Registro_Productos'

    def __str__(self) -> str:
        return self.Nombre_Producto