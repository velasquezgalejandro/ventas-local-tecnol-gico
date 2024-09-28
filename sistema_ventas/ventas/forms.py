from django import forms
from .models import Producto, Categoria, Cliente, Venta

### -------------------------------------------- ###
# producto Form
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'descripcion', 'precio', 'stock' ]

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('El nombre de la categoria es obligatorio.')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre de la categoria debe tener al menos 3 caracteres.')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')

        if precio is None:
            raise forms.ValidationError('El precio es obligatorio.')

        if precio <= 0:
            raise forms.ValidationError('El precio debe ser un número positivo mayor a 0.')

        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')

        if stock is None:
            raise forms.ValidationError('El stock es obligatorio.')

        if stock < 0:
            raise forms.ValidationError('El stock debe ser un número entero no negativo.')

        return stock

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
            raise forms.ValidationError('El nombre de la categoria debe tener al menos 3 caracteres.')
        return nombre


### -------------------------------------------- ###
# cliente Form
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('El nombre de la categoria es obligatorio.')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre de la categoria debe tener al menos 3 caracteres.')
        return nombre

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError('El correo electrónico es obligatorio.')

        try:
            forms.EmailField().clean(email)
        except forms.ValidationError:
            raise forms.ValidationError('El correo electrónico no es válido.')

        return email

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        if not telefono:
            raise forms.ValidationError('El número de teléfono es obligatorio.')

        if len(telefono) < 7 or not telefono.isdigit():
            raise forms.ValidationError('El número de teléfono debe contener al menos 7 dígitos y solo números.')
        return telefono

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if not direccion:
            raise forms.ValidationError('La dirección es obligatoria.')
        if len(direccion) < 10:
            raise forms.ValidationError('La dirección debe tener al menos 10 caracteres.')
        return direccion

### -------------------------------------------- ###
# ventas form
class VentasForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto' ,'cliente' ,'cantidad']
