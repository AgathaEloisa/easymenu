"""Vistas del módulo de administración"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import productos, Menu
from .forms import ProductoForm, MenuForm

@login_required
def AdminView(request):
    products = productos.objects.all()
    menus = Menu.objects.all()
    context = {
        'products': products,
        'menus' : menus
    }
    return render(request, 'admin/admin.html', context)

def NuevoProductoView(request):
    products = productos.objects.all() 
    last_product = products.last().numeroProducto if products else 0
    initial_data = {'numeroProducto': last_product + 1} if last_product else {'numeroProducto': 1}
    form = ProductoForm(initial=initial_data)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            numeroProducto = form.cleaned_data['numeroProducto']
            categoria = form.cleaned_data['categoria']
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            descripcion = form.cleaned_data['descripcion']
            p, created = productos.objects.get_or_create(numeroProducto=numeroProducto,categoria=categoria,nombre=nombre,precio=precio,descripcion=descripcion)
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
    prod = productos.objects.get(numeroProducto=numeroProducto)
    form = ProductoForm(request.POST or None, instance=prod)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('administracion:home')
    return render(request, 'admin/editar_producto.html',{'prod':prod, 'form': form})

def eliminarProductoView(request, numeroProducto):
    prod = productos.objects.filter(numeroProducto = numeroProducto)
    if request.method == 'POST':
        prod.delete()
        return redirect('administracion:home')
    return render(request, 'admin/eliminar_producto.html', {'prod':prod})

# Menu
def NuevoMenuView(request):
    products = productos.objects.all()
    menu = Menu.objects.all()
    last_menu = menu.last().numeroMenu if menu else 0
    initial_data = {'numeroProducto': last_menu + 1} if last_menu else {'numeroProducto': 1}
    form = MenuForm(initial=initial_data)
    context = {
        'form': form,
        'products': products
    }

    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            numeroMenu = form.cleaned_data['numeroMenu']
            nombre = form.cleaned_data['nombre']
            fechaCreacion = form.cleaned_data['fechaCreacion']
            producto = form.cleaned_data['productos']
            descripcion = form.cleaned_data['descripcion']
            p, created = productos.objects.get_or_create(numeroMenu=numeroMenu,nombre=nombre,fechaCreacion=fechaCreacion,producto=producto, descripcion=descripcion)
            p.save()
            return redirect('administracion:home')

    return render(request, 'admin/nuevo_menu.html', context)