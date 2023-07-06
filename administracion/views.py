from django.views.generic import View, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import carta, productos
from .forms import ProductoForm
from django.urls import reverse_lazy

@login_required
def AdminView(request):
    products = productos.objects.all()
    context = {
        'products': products
    }
    return render(request, 'admin/admin.html', context)

def NuevoProductoView(request):
    form = ProductoForm()
    context = {
        'form': form
    }
    products = productos.objects.all()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            numeroProducto = int(len(products)+1)
            categoria = form.cleaned_data['categoria']
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            descripcion = form.cleaned_data['descripcion']
            
            p, created = productos.objects.get_or_create(numeroProducto=numeroProducto, categoria=categoria, nombre=nombre, precio=precio, descripcion=descripcion)
            p.save()
            
            return redirect('administracion:home')
    
    return render(request, 'admin/nuevo_producto.html', context)

def detalleProductoView(request, numeroProducto):
    prod = get_object_or_404(productos, numeroProducto = numeroProducto)
    context = {
        'prod': prod
    }
    return render(request, 'admin/detalle_producto.html', context)

def EditarProductoView(request, numeroProducto):
    prod = get_object_or_404(productos, numeroProducto = numeroProducto)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=prod)
    if form.is_valid():
        form.save()
        return redirect('administracion:detalle_producto')
    return render(request, 'admin/editar_producto.html',{'form':form})

def eliminarProductoView(request, numeroProducto):
    prod = productos.objects.filter(numeroProducto = numeroProducto)
    if request.method == 'POST':
        prod.delete()
        return redirect('administracion:home')
    return render(request, 'admin/eliminar_producto.html', {'prod':prod})
