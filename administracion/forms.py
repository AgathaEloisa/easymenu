from django import forms
# from django.db import forms
from .models import productos, Menu
from djongo import models

class DateInput(forms.DateInput):
    input_type = 'date'
class ProductoForm(forms.ModelForm):
    numeroProducto = forms.IntegerField(required=True)
    categoria = forms.CharField(required=True)
    nombre = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    descripcion = models.TextField(max_length=250)
    class Meta:
        model = productos
        fields = ("numeroProducto","categoria","nombre","precio","descripcion")

class MenuForm(forms.ModelForm, forms.Form):
    fechaCreacion = forms.DateField(widget=DateInput)
    class Meta:
        model = Menu
        fields = ("numeroMenu", "nombre", "fechaCreacion", "producto", "descripcion")
