from django.db import models
from administracion.models import Producto
from djongo import models

class Orden(models.Model):
    numeroOrden = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    mesa = models.IntegerField()
    mesero = models.IntegerField()
    codigoEstado = models.IntegerField()
    productos = models.ManyToManyField(Producto, through='OrdenProducto', blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numeroOrden

    class Meta:
        db_table = 'orden' 

class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE,db_column='numeroOrden')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,db_column='numeroProducto')
    cantidad = models.IntegerField(default=1)
    notas = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.orden} - {self.producto} - {self.cantidad}"
    