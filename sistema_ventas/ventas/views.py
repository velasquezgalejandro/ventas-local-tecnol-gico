from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

# vista para acciones de productos
def productos(request):
    return render(request, 'productos.html')

# vista para acciones de clientes
def clientes(request):
    return render(request, 'clientes.html')

# vista para acciones de ventas
def ventas(request):
    return render(request, 'ventas.html')
