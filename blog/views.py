from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicar
# Create your views here.
def listar(request):
    articulos = Publicar.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'articulos':articulos})

def detalle(request, pk):
    pub = get_object_or_404(Publicar, pk=pk)
    return render(request, 'blog/detalle.html', {'pub': pub})
