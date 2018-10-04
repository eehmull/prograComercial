from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicar
from .form import PubForm
# Create your views here.
def listar(request):
    articulos = Publicar.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'articulos':articulos})

def detalle(request, pk):
    pub = get_object_or_404(Publicar, pk=pk)
    return render(request, 'blog/detalle.html', {'pub': pub})

def nuevo(request):
    if request.method == "POST":
        formulario = PubForm(request.POST)
        if formulario.is_valid():
            p = formulario.save(commit=False)
            p.autor = request.user
            p.fecha_publicacion = timezone.now()
            p.save()
            return redirect('listar')
    else:
        formulario = PubForm()
    return render(request, 'blog/editar.html', {'formulario': formulario})
