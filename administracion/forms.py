from django import forms
from .models import productos, carta

class ProductoForm(forms.ModelForm):
    numeroProducto = forms.IntegerField(required=True, disabled=True)
    categoria = forms.CharField(required=True)
    nombre = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    class Meta:
        model = productos
        fields = ("numeroProducto","categoria","nombre","precio","descripcion")
