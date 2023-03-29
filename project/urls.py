"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seguros.views import index, autos_1, hogar_1, vida_1, agregar_post, buscar_post

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('rama-autos/', autos_1, name="autos"),
    path('rama-hogar/', hogar_1, name="hogar"),
    path('rama-vida/', vida_1, name="vida"),
    path('rama-autos/agregar', agregar_post, name="agregar-post"),
    path('rama-autos/buscar', buscar_post, name="buscar-post"),
]
