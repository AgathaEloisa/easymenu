from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('intranet/', include('administracion.urls'), name='administracion'),
    path('', include('menu.urls'), name='menu'),
    path('pedidos/', include('pedidos.urls'), name='pedidos')
]
