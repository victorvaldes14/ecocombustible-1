from django.db import models
from django.contrib.auth.models import User

class Prestador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=120)
    comuna = models.CharField(max_length=120)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email_contacto = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    TIPOS = [
        ('corte', 'Corte de leña'),
        ('picado', 'Picado'),
        ('transporte', 'Transporte'),
        ('limpieza', 'Limpieza de cañones'),
    ]
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    titulo = models.CharField(max_length=160)
    descripcion = models.TextField(blank=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    comuna = models.CharField(max_length=120)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"
