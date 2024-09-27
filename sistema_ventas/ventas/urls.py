from django.urls import path
from .views import inicio, clientes, productos, ventas

urlpatterns = [
    path('', inicio, name='inicio'),  # Ruta para la página de inicio
    path('clientes/', clientes, name='clientes'),  # Ruta para la página de clientes
    path('productos/', productos, name='productos'),  # Ruta para la página de productos
    path('ventas/', ventas, name='ventas'),  # Ruta para la página de ventas
]
