from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Categoria, Cliente
from .forms import CategoriaForm, ClienteForm

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

### -------------------------------------------------------------------###
# vista para acciones de ventas
def ventas(request):
    return render(request, 'ventas.html')
