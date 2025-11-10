from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .models import Servicio, Prestador
from .forms import ServicioForm

def lista_servicios(request):
    filtro_tipo = request.GET.get('tipo')
    filtro_comuna = request.GET.get('comuna')
    servicios = Servicio.objects.select_related('prestador').all()

    if filtro_tipo:
        servicios = servicios.filter(tipo=filtro_tipo)
    if filtro_comuna:
        servicios = servicios.filter(comuna__icontains=filtro_comuna)

    return render(request, 'servicios/lista.html', {'servicios': servicios})

@login_required
def crear_servicio(request):
    prestador = Prestador.objects.get(usuario=request.user)
    form = ServicioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        servicio = form.save(commit=False)
        servicio.prestador = prestador
        servicio.save()
        servicios = Servicio.objects.select_related('prestador').all()
        html = render_to_string('servicios/lista.html', {'servicios': servicios}, request)
        return HttpResponse(html)
    html = render_to_string('servicios/_formulario.html', {'form': form}, request)
    return HttpResponse(html)

@login_required
def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk, prestador__usuario=request.user)
    form = ServicioForm(request.POST or None, instance=servicio)
    if request.method == 'POST' and form.is_valid():
        form.save()
        servicios = Servicio.objects.select_related('prestador').all()
        html = render_to_string('servicios/lista.html', {'servicios': servicios}, request)
        return HttpResponse(html)
    html = render_to_string('servicios/_formulario.html', {'form': form}, request)
    return HttpResponse(html)

@login_required
def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk, prestador__usuario=request.user)
    servicio.delete()
    return HttpResponse('')
