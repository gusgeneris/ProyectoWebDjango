from turtle import update
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length= 50)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nombre
    
class Posteo(models.Model):
    titulo = models.CharField(max_length= 50)
    contenido = models.CharField(max_length= 50)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #se crea una clave foranea de relacion entre los usuarios registrados para que puedan agregarce como autores
    categorias = models.ManyToManyField(Categoria) #se crea una relacion de muchos a muchos para que un post pueda tener varias categorias y biceversa
    
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'posteo'
        verbose_name_plural = 'posteos'
    
    def __str__(self):
        return self.titulo