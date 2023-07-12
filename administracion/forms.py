from django import forms
from .models import Producto
from djongo import models

class ProductoForm(forms.ModelForm):
    numeroProducto = forms.IntegerField(required=True, widget = forms.TextInput(attrs={'readonly':'readonly'}))
    categoria = forms.CharField(required=True)
    nombre = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    descripcion = models.TextField(max_length=250)
    class Meta:
        model = Producto
        fields = ("numeroProducto","categoria","nombre","precio","descripcion")
