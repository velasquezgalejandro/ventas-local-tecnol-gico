from django.urls import path
from .views import inicio, categorias, listar_categorias, agregar_categoria, editar_categoria, detalle_categoria, eliminar_categoria, clientes, listar_clientes, agregar_clientes, detalle_cliente, editar_cliente, eliminar_cliente, productos, listar_productos, agregar_producto, detalle_producto, editar_producto, eliminar_producto, ventas, listar_ventas, agregar_venta, detalle_venta, editar_venta, eliminar_venta


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

# productos
    path('productos/listar/', listar_productos, name='listar_productos'),
    path('productos/agregar/', agregar_producto, name='agregar_producto'),
    path('productos/detalle/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('productos/editar/<int:pk>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),

# ventas
    path('ventas/listar/', listar_ventas, name='listar_ventas'),
    path('ventas/agregar/', agregar_venta, name='agregar_venta'),
    path('ventas/detalle/<int:pk>/', detalle_venta, name='detalle_venta'),
    path('ventas/editar/<int:pk>/', editar_venta, name='editar_venta'),
    path('ventas/eliminar/<int:pk>/', eliminar_venta, name='eliminar_venta'),
]
