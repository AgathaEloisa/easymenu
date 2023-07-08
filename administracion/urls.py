"""Rutas del módulo de administración"""
from django.urls import path
from .views import AdminView, NuevoProductoView, detalleProductoView
from .views import EditarProductoView, eliminarProductoView
app_name = 'administracion'

urlpatterns = [
    path('', AdminView, name='home'),
    path('nuevo_producto/', NuevoProductoView, name='nuevo_producto'),
    path('editar_producto/<int:numeroProducto>/', EditarProductoView, name='editar_producto'),
    path('detalle_producto/<int:numeroProducto>/', detalleProductoView, name='detalle_producto'),
    path('eliminar_producto/<int:numeroProducto>/', eliminarProductoView, name='eliminar_producto')
]
