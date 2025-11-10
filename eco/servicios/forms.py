from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['tipo', 'titulo', 'descripcion', 'precio_base', 'comuna']
        labels = {
            'tipo': 'Tipo de servicio',
            'titulo': 'Título del servicio',
            'descripcion': 'Descripción',
            'precio_base': 'Precio base (CLP)',
            'comuna': 'Comuna donde se ofrece',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
