#from django.db import models

#class Post(models.Model):
#    pass

#nuevo

from django.db import models

class Post(models.Model):
     Suma_asegurada = models.CharField(max_length=40)
     Suma_description = models.CharField(max_length=80)
     heading = models.CharField(max_length=100)
    
   
     def __str__(self):
        return f"{self.id} - {self.Suma_description} - {self.heading} "