from django import forms
from .models import Producto, Categoria, Cliente, Venta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'proveedor', 'etiquetas', 'cantidad', 'precio', 'descripcion']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre' ,'telefono' ,'email' ,'direccion']

class VentasForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto' ,'cliente' ,'cantidad']
