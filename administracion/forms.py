from django import forms
# from django.db import forms
from .models import Producto
from djongo import models

class ProductoForm(forms.ModelForm):
    numeroProducto = forms.IntegerField(required=True)
    categoria = forms.CharField(required=True)
    nombre = forms.CharField(required=True)
    precio = forms.DecimalField(required=True)
    descripcion = models.TextField(max_length=250)
    class Meta:
        model = Producto
        fields = ("numeroProducto","categoria","nombre","precio","descripcion")
