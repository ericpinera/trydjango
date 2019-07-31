from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "mi_texto" : "Texto sobre nosotros",
        "mi_numero" : 12345,
        "mi_lista" : [123,456,300,678,"ABC"]
    }
    return render(request, "about.html", my_context)
