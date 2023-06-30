from django.db import models

class carta(models.Model):
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
    # _id = models.ObjectIdField()
    categoria = models.CharField(max_length=50)
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.nombre
