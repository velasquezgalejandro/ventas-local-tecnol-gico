# Create your models here.
from django.db import models

# modelo de producto
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

# modelo de cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

# modelo de Venta
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Venta de {self.cantidad} {self.producto.nombre} a {self.cliente.nombre}"
