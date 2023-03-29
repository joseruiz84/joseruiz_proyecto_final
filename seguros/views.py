from django.shortcuts import render
from seguros.models import Post
from seguros.forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DetailView

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

class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post
    context_object_name = "post"

class PostUpdate( UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'