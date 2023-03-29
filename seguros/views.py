from django.shortcuts import render
from seguros.models import Post
from seguros.forms import PostForm

def index(request):
    return render(request, "seguros/index.html")

def autos_1(request):
   
    context = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }

    return render(request, "seguros/autos.html", context)

def hogar_1(request):
    return render(request, "seguros/hogar.html")

def vida_1(request):
    return render(request, "seguros/vida.html")

def agregar_post(request):
    post_form = PostForm(request.POST)
    post_form.save()
    
    context = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }

    return render(request, "seguros/autos.html", context)

def buscar_post(request):
    criterio = request.GET.get("criterio")
    context = {
        "posts": Post.objects.filter(Suma_description__icontains=criterio).all(),
    }
    return render(request, "seguros/autos.html", context)