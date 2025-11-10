from django.db import models
from django.contrib.auth.models import User

class Proveedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_empresa = models.CharField(max_length=120)
    comuna = models.CharField(max_length=120)
    codigo_sncl = models.CharField(max_length=64, blank=True, null=True)
    sncl_validado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_empresa


class Producto(models.Model):
    TIPO_PRODUCTO = [
        ('lenia', 'Leña'),
        ('pellet', 'Pellet'),
        ('carbon', 'Carbón'),
        ('briqueta', 'Briquetas'),
    ]

    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=16, choices=TIPO_PRODUCTO)
    nombre = models.CharField(max_length=160)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.proveedor.nombre_empresa}"
