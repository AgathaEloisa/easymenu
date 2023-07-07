from django.db import models
from djongo import models
import uuid

class carta(models.Model):
    #  _id = models.ObjectIdField()
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=False)
    # productos = models.ForeignKey(productos, related_name='productos')
    productos = [models.IntegerField()]
    # productos = models.ArrayReferenceField(
    #     to=productos,
    #     blank=True,
    #     on_delete=models.DO_NOTHING
    # )

    def __str__(self) -> str:
        return self.nombre
    
class productos(models.Model):
    # id = models.ObjectIdField()
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numeroProducto = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = 'productos'