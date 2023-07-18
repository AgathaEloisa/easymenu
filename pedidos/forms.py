from django import forms
from menu.models import Orden

class TotalInput(forms.TextInput):
    def get_context(self, name, value, attrs):
        return super().get_context(name, value, attrs)

class OrdenForm(forms.ModelForm):
    numeroOrden=forms.IntegerField(required=True, widget = forms.TextInput(attrs={'readonly':'readonly'}))
    total = forms.DecimalField(widget=TotalInput)

    class Meta:
        model = Orden
        fields = ['numeroOrden', 'mesa', 'mesero', 'codigoEstado', 'productos', 'total']