from typing import Any
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
    
class Producto(models.Model):
    numeroProducto = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = 'Producto'