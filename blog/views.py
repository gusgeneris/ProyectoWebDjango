from django.shortcuts import render
from blog.models import Posteo , Categoria

# Create your views here.

def blog(request):
    
    posteos = Posteo.objects.all()
    categorias = Categoria.objects.all()
    
    return render (request,'blog/blog.html',{'posteos':posteos})