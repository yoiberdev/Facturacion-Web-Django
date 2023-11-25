from django.db import models
from datetime import datetime


# Create your models here.
class Cliente(models.Model):
    cliente = models.CharField(max_length=200)
    dni = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    def __str__(self):
        return self.cliente


class Venta(models.Model):
    ruc = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=datetime.now, blank=True) 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Producto(models.Model):
    producto = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    cantidad = models.IntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.producto} {self.precio} {self.cantidad}"
