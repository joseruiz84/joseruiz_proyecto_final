from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
     Suma_asegurada = models.CharField(max_length=40)
     Suma_description = models.CharField(max_length=80)
     heading = models.CharField(max_length=100)
     mail = models.CharField(max_length=60)
     telefono = models.CharField(max_length=20)
     publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
   
     def __str__(self):
        return f"{self.id} - {self.Suma_description} - {self.heading} "