from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicar
from .form import PubForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def listar(request):
    articulos = Publicar.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'articulos':articulos})

@login_required
def detalle(request, pk):
    pub = get_object_or_404(Publicar, pk=pk)
    return render(request, 'blog/detalle.html', {'pub': pub})

@login_required
def nuevo(request):
    if request.method == "POST":
        formulario = PubForm(request.POST)
        if formulario.is_valid():
            p = formulario.save(commit=False)
            p.autor = request.user
            #p.fecha_publicacion = timezone.now()
            p.save()
            return redirect('listar')
    else:
        formulario = PubForm()
    return render(request, 'blog/editar.html', {'formulario': formulario})

@login_required
def editar(request, pk):
    formulario = get_object_or_404(Publicar, pk=pk)
    if request.method == "POST":
        formulario = PubForm(request.POST, instance=formulario)
        if formulario.is_valid():
            pub = formulario.save(commit=False)
            pub.autor = request.user
            #pub.fecha_publicacion = timezone.now()
            pub.save()
            return redirect('editar', pk=pub.pk)
    else:
        formulario = PubForm(instance=formulario)
    return render(request, 'blog/editar.html', {'formulario': formulario})

@login_required
def borrador(request):
    articulos = Publicar.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/borrador.html', {'articulos': articulos})

@login_required
def publicarborrador(request, pk):
    pub = get_object_or_404(Publicar, pk=pk)
    pub.publicar()
    return redirect('detalle', pk=pk)

@login_required
def remover(request, pk):
    formulario = get_object_or_404(Publicar, pk=pk)
    formulario.delete()
    return redirect('listar')
