from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoriaForm
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Categoria

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
    return render(request, 'categorias/eliminar_producto.html', {'categoria': categoria})

### -------------------------------------------------------------------###
# vista para acciones de clientes
def clientes(request):
    return render(request, 'clientes.html')

### -------------------------------------------------------------------###
# vista para acciones de productos
def productos(request):
    return render(request, 'productos.html')

### -------------------------------------------------------------------###
# vista para acciones de ventas
def ventas(request):
    return render(request, 'ventas.html')
