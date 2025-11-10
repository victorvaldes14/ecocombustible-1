from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .models import Producto, Proveedor
from .forms import ProductoForm

def lista_productos(request):
    productos = Producto.objects.select_related('proveedor').all()
    return render(request, 'catalogo/lista.html', {'productos': productos})

@login_required
def crear_producto(request):
    proveedor = Proveedor.objects.get(usuario=request.user)
    form = ProductoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        producto = form.save(commit=False)
        producto.proveedor = proveedor
        producto.save()
        productos = Producto.objects.select_related('proveedor').all()
        html = render_to_string('catalogo/lista.html', {'productos': productos}, request)
        return HttpResponse(html)
    html = render_to_string('catalogo/_formulario.html', {'form': form}, request)
    return HttpResponse(html)

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, proveedor__usuario=request.user)
    form = ProductoForm(request.POST or None, instance=producto)
    if request.method == 'POST' and form.is_valid():
        form.save()
        productos = Producto.objects.select_related('proveedor').all()
        html = render_to_string('catalogo/lista.html', {'productos': productos}, request)
        return HttpResponse(html)
    html = render_to_string('catalogo/_formulario.html', {'form': form}, request)
    return HttpResponse(html)

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, proveedor__usuario=request.user)
    producto.delete()
    return HttpResponse('')
