from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrdenForm
from menu.models import Orden
# from django.urls import reverse_lazy

def actualizar_orden(request, numeroOrden):
    orden = get_object_or_404(Orden, numeroOrden=numeroOrden)
    form = OrdenForm(request.POST or None, instance=orden)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pedidos:ver_ordenes')
    return render(request, 'pedidos/actualizar_orden.html', {'orden': orden, 'form': form})

def ver_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'pedidos/ver_ordenes.html', {'ordenes': ordenes})

def ver_orden(request, numeroOrden):
    orden = get_object_or_404(Orden, numeroOrden=numeroOrden)
    return render(request, 'pedidos/ver_orden.html', {'orden': orden})

def borrar_orden(request, numeroOrden):
    orden = get_object_or_404(Orden, numeroOrden=numeroOrden)
    if request.method == 'POST':
        orden.delete()
        return redirect('pedidos:ver_ordenes')
    return render(request, 'pedidos/borrar_orden.html', {'orden': orden})
