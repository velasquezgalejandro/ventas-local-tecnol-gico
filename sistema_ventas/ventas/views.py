from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Categoria, Cliente, Producto, Venta
from .forms import CategoriaForm, ClienteForm, ProductoForm, VentasForm

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

### -------------------------------------------------------------------###
# vista para acciones de categorias
def categorias(request):
    return render(request, 'categorias.html')

#lista
def listar_categorias(request):
    categorias_list = Categoria.objects.all()
    query = request.GET.get('q')

    if query:
        categorias_list = categorias_list.filter(Q(nombre__icontains = query))

    paginator = Paginator(categorias_list, 10)
    page_number = request.GET.get('page')
    categorias = paginator.get_page(page_number)

    return render(request, 'categorias/listar_categorias.html', {'categorias': categorias})

# agrega
def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/crear_categorias.html', {'form':form})

# detalle
def detalle_categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    return render(request, 'categorias/detalle_categoria.html', {'categoria': categoria})

# edita
def editar_categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/editar_categoria.html', {'form': form})

# elimina
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'categorias/eliminar_categoria.html', {'categoria': categoria})

### -------------------------------------------------------------------###
# vista para acciones de clientes
def clientes(request):
    return render(request, 'clientes.html')

#lista
def listar_clientes(request):
    clientes_list = Cliente.objects.all()
    query = request.GET.get('q')

    if query:
        clientes_list = clientes_list.filter(Q(nombre__icontains = query))

    paginator = Paginator(clientes_list, 10)
    page_number = request.GET.get('page')
    clientes = paginator.get_page(page_number)

    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

# agrega
def agregar_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/crear_clientes.html', {'form':form})


# detalle
def detalle_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente})

# edita
def editar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form})


# elimina
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})

### -------------------------------------------------------------------###
# vista para acciones de productos
def productos(request):
    return render(request, 'productos.html')

#lista
def listar_productos(request):
    producto_list = Producto.objects.all()
    query = request.GET.get('q')

    if query:
        producto_list = producto_list.filter(Q(nombre__icontains = query))

    paginator = Paginator(producto_list, 10)
    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)

    return render(request, 'productos/listar_productos.html', {'productos': productos})

# agrega
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form':form})

# detalle
def detalle_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

# edita
def editar_producto(request, pk):
    cliente = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=cliente)
    return render(request, 'productos/editar_producto.html', {'form': form})

# elimina
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

### -------------------------------------------------------------------###
# vista para acciones de ventas
def ventas(request):
    return render(request, 'ventas.html')

#lista
def listar_ventas(request):
    ventas_list = Venta.objects.all()
    query = request.GET.get('q')

    if query:
        ventas_list = ventas_list.filter(Q(nombre__icontains = query))

    paginator = Paginator(ventas_list, 10)
    page_number = request.GET.get('page')
    ventas = paginator.get_page(page_number)

    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas})

# agrega
def agregar_venta(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)  # No guardar todavía
            producto = venta.producto
            venta.total = producto.precio * venta.cantidad
            venta.save()
            producto.stock -= venta.cantidad
            producto.save()
            return redirect('listar_ventas')
    else:
        form = VentasForm()
    return render(request, 'ventas/agregar_venta.html', {'form':form})

# detalle
def detalle_venta(request, pk):
    venta = Venta.objects.get(pk=pk)
    return render(request, 'ventas/detalle_venta.html', {'venta': venta})

# edita
def editar_venta(request, pk):
    cliente = Venta.objects.get(pk=pk)
    if request.method == 'POST':
        form = VentasForm(request.POST, instance=cliente)
        if form.is_valid():
            venta = form.save(commit=False)  # No guardar todavía
            producto = venta.producto
            venta.total = producto.precio * venta.cantidad
            venta.save()
            producto.stock -= venta.cantidad
            producto.save()
            return redirect('listar_ventas')
    else:
        form = VentasForm(instance=cliente)
    return render(request, 'ventas/editar_venta.html', {'form': form})

# elimina
def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('listar_ventas')
    return render(request, 'ventas/eliminar_venta.html', {'venta': venta})
