from django.db import models
from django.contrib.auth.models import User



class Zapatilla(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='zapatillas')

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    marca = models.CharField(max_length=100)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.marca

    
    
    

