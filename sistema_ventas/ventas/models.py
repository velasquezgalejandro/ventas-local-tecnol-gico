# Create your models here.
from django.db import models

# modelo de categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.nombre)

# modelo de producto
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

# modelo de cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, help_text='Ingresar el telefono sin indicadores')
    direccion = models.CharField(max_length=300, help_text='La direccion debe ser copiada en formato completo por ej: calle 1 #1A22')

    def __str__(self):
        return self.nombre

# modelo de Venta
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateField(help_text='La fecha debe estar en el formato dd/mm/yyyy')
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta de {self.cantidad} {self.producto.nombre} a {self.cliente.nombre}"
