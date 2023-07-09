from typing import Any
from django.db import models
from djongo import models
import uuid

class productos(models.Model):
    numeroProducto = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = 'productos'

class Menu(models.Model):
    numeroMenu = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    fechaCreacion = models.DateField(auto_now=False, auto_now_add=False)
    # productos = [models.IntegerField()]
    producto = models.ArrayReferenceField(
        to=productos,
        blank=True,
        on_delete=models.DO_NOTHING
    )

    def __str__(self) -> str:
        return self.nombre