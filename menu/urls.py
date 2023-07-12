from django.urls import path
from .views import mostrar_productos, agregar_al_carrito, ver_carrito, eliminar_del_carrito

app_name='menu'

urlpatterns = [
    path('', mostrar_productos, name='menu'),
    path('agregar_al_carrito/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/', eliminar_del_carrito, name='eliminar_del_carrito'),
]
