from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm, RawProductoForm

from .models import Producto

# Create your views here.
# def producto_crear_view(request):
#     formulario = RawProductoForm()
#     if request.method == "POST":
#         formulario = RawProductoForm(request.POST)
#         if formulario.is_valid():
#             print(formulario.cleaned_data)
#             Producto.objects.create(**formulario.cleaned_data)
#         else:
#             print(formulario.errors)
#     context = {
#         "form" : formulario
#     }
#     return render(request, "productos/producto_crear.html", context)



# def producto_crear_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == 'POST':
#         titulo = request.POST.get('title')
#         print(titulo)
#     context = {}    
#     return render(request, "productos/producto_crear.html", context)

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
    context = {
        'Objeto':obj
    }    
    return render(request, "productos/producto_detalle.html", context)

def vista_dinamica_producto(request, uid):
    #objeto = Producto.objects.get(id=uid)
    objeto = get_object_or_404(Producto, id=uid)
    contexto = {
        'Objeto': objeto
    }
    return render(request, "productos/producto_detalle.html", contexto)


