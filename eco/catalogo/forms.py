from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['tipo', 'nombre', 'descripcion', 'precio', 'stock']
        labels = {
            'tipo': 'Tipo de producto',
            'nombre': 'Nombre del producto',
            'descripcion': 'Descripción',
            'precio': 'Precio (CLP)',
            'stock': 'Cantidad disponible',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
