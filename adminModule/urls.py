from django.urls import path, include
from .views import AdminView


app_name = 'adminModule'

urlpatterns = [
    path('', AdminView.as_view(), name='home')
]
