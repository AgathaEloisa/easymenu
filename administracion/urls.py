from django.urls import path
from .views import AdminView

app_name = 'administracion'

urlpatterns = [
    path('', AdminView, name='home')
]
