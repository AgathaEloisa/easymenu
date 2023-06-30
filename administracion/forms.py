from django import forms
from .models import productos, carta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = ("categoria","codigo","nombre","precio","descripcion")
