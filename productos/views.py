from django.shortcuts import render

from .forms import ProductoForm

from .models import Producto

# Create your views here.
def producto_crear_view(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    form = ProductoForm()    
        
    context = {
        'form':form
    }    
    return render(request, "productos/producto_crear.html", context)


def producto_detalles_view(request):
    obj = Producto.objects.get(id=1)
    
    #context = {
    #    'titulo': obj.titulo,
    #    'descripcion': obj.descripcion
    #}
    
    context = {
        'Objeto':obj
    }
    
    return render(request, "productos/producto_detalle.html", context)
