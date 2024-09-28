from django.urls import path
from .views import inicio, categorias, listar_categorias, agregar_categoria, editar_categoria, detalle_categoria, eliminar_categoria, clientes, listar_clientes, agregar_clientes, detalle_cliente, editar_cliente, eliminar_cliente, productos, ventas

urlpatterns = [
    path('', inicio, name='inicio'),  # Ruta para la página de inicio
    path('categorias/', categorias, name='categorias'),  # Ruta para la página de categorias
    path('clientes/', clientes, name='clientes'),  # Ruta para la página de clientes
    path('productos/', productos, name='productos'),  # Ruta para la página de productos
    path('ventas/', ventas, name='ventas'),  # Ruta para la página de ventas

# categorias
    path('categorias/listar/', listar_categorias, name='listar_categorias'),
    path('categorias/agregar/', agregar_categoria, name='agregar_categoria'),
    path('categorias/detalle/<int:pk>/', detalle_categoria, name='detalle_categoria'),
    path('categorias/editar/<int:pk>/', editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', eliminar_categoria, name='eliminar_categoria'),

# clientes
    path('clientes/listar/', listar_clientes, name='listar_clientes'),
    path('clientes/agregar/', agregar_clientes, name='agregar_clientes'),
    path('clientes/detalle/<int:pk>/', detalle_cliente, name='detalle_cliente'),
    path('clientes/editar/<int:pk>/', editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),
]
