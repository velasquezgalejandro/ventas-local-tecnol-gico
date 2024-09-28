from django import forms
from .models import Producto, Categoria, Cliente, Venta

### -------------------------------------------- ###
# producto Form
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'descripcion', 'precio', 'stock' ]

### -------------------------------------------- ###
# categoria Form
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('El nombre de la categoria es obligatorio.')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre de la categoria debe tener al menos 4 caracteres.')
        return nombre


### -------------------------------------------- ###
# cliente Form
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre' , 'telefono' ,'email' ,'direccion']

### -------------------------------------------- ###
# ventas form
class VentasForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto' ,'cliente' ,'cantidad']
