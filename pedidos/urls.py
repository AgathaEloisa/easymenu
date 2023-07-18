from django.urls import path
from .views import ver_ordenes, ver_orden, actualizar_orden, borrar_orden

app_name = 'pedidos'	
			
urlpatterns = [
    # path('crear/', crear_orden, name='crear_orden'),
    path('', ver_ordenes, name='ver_ordenes'),
    path('ver/<int:numeroOrden>/', ver_orden, name='ver_orden'),
    path('actualizar/<int:numeroOrden>/', actualizar_orden, name='actualizar_orden'),
    path('borrar/<int:numeroOrden>/', borrar_orden, name='borrar_orden'),
]