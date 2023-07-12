from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, DeleteView
from django.urls import reverse_lazy
from administracion.models import Producto
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import Orden
from django.utils import timezone
from uuid import uuid4
from .models import OrdenProducto
import random

def mostrar_productos(request):
    categoria = request.GET.get('categoria')
    productos = Producto.objects.all()

    if categoria:
        productos = productos.filter(categoria=categoria)

    return render(request, 'menu/menu_productos.html', {'productos': productos, 'categoria': categoria})



def agregar_al_carrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 1))

        carrito = request.session.get('carrito', [])
        for _ in range(cantidad):
            carrito.append(producto_id)
        request.session['carrito'] = carrito

    return redirect('menu:menu')

def ver_carrito(request):
    if request.method == 'POST':
        numero_mesa = request.POST.get('numero_mesa', 'N/A')
        producto_id = request.POST.get('producto_id')
        notas = request.POST.get('notas')

        # Obtener las notas actuales de la sesión
        notas_dict = request.session.get('notas', {})

        # Guardar las notas en el diccionario de notas
        notas_dict[str(producto_id)] = notas

        # Actualizar la sesión con las notas actualizadas
        request.session['notas'] = notas_dict
        request.session['numero_mesa'] = numero_mesa

        if numero_mesa == 'N/A':
            # Manejar el caso cuando 'numero_mesa' no está presente en la solicitud POST
            messages.error(request, 'Error: El número de mesa no se proporcionó correctamente.')
            return redirect('menu:ver_carrito')

        # Obtener los productos del carrito
        carrito = request.session.get('carrito', [])
        productos = Producto.objects.filter(numeroProducto__in=carrito)
        total_precio = 0

        # Obtener el último número de orden utilizado
        try:
            ultimo_numero_orden = Orden.objects.latest('numeroOrden').numeroOrden
        except Orden.DoesNotExist:
            ultimo_numero_orden = 0

        # Generar el siguiente número de orden
        siguiente_numero_orden = ultimo_numero_orden + 1

        # Crear una nueva orden
        mesero = random.randint(0, 5)
        orden = Orden(numeroOrden=siguiente_numero_orden, fecha=timezone.now(), mesa=numero_mesa, mesero=mesero, codigoEstado=0, total=0)
        orden.save()

        # Asociar los productos seleccionados a la orden
        for producto in productos:
            cantidad = carrito.count(producto.numeroProducto)
            orden_producto = OrdenProducto(orden=orden, producto=producto, cantidad=cantidad, notas=notas_dict.get(str(producto.numeroProducto), ''))  # Agregado el campo 'notas'
            orden_producto.save()
            total_precio += int(str(producto.precio)) * cantidad

        # Actualizar el total de la orden
        orden.total = total_precio
        orden.save()

        # Limpiar el carrito y la sesión
        request.session.pop('carrito', [])
        request.session.pop('numero_mesa', None)
        request.session.pop('notas', None)

        return redirect('menu:menu')

    else:
        notas = request.session.get('notas', '')
        numero_mesa = request.session.get('numero_mesa', 'N/A')

    carrito = request.session.get('carrito', [])
    productos = Producto.objects.filter(numeroProducto__in=carrito)
    carrito_productos = []
    total_precio = 0

    # Obtener las notas para cada producto del carrito
    notas_dict = request.session.get('notas', {})
    carrito_productos = []
    total_precio = 0

    for producto in productos:
        cantidad = carrito.count(producto.numeroProducto)+1
        precio_total = int(str(producto.precio)) * cantidad
        notas = notas_dict.get(str(producto.numeroProducto), '')  # Obtener las notas correspondientes al producto
        carrito_productos.append({'producto': producto, 'cantidad': cantidad, 'precio_total': precio_total, 'notas': notas})
        total_precio += precio_total

    context = {
        'carrito_productos': carrito_productos,
        'total_precio': total_precio,
        'numero_mesa': numero_mesa,
        'notas': notas,
    }
    return render(request, 'menu/carrito.html', context)


def eliminar_del_carrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        carrito = request.session.get('carrito', [])
        if producto_id in carrito:
            carrito.remove(producto_id)
            request.session['carrito'] = carrito
            messages.success(request, 'El producto ha sido eliminado del carrito.')
    return redirect('menu:ver_carrito')