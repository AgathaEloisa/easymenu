from typing import Any
from django.db import models
from djongo import models

class Producto(models.Model):
    numeroProducto = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = 'Producto'