from django.shortcuts import render
from seguros.models import Post
from seguros.forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

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
        "posts": Post.objects.filter(heading__icontains=criterio).all(),
    }
    return render(request, "seguros/autos.html", context)

class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post
    context_object_name = "post"

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = reverse_lazy("post-list")

class Login(LoginView):
    next_page = reverse_lazy('post-list')

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('post-list')