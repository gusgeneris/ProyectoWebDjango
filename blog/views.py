from django.shortcuts import render
from blog.models import Posteo , Categoria

# Create your views here.

def blog(request):
    
    posteos = Posteo.objects.all()
    categorias = Categoria.objects.all()
    
    return render (request,'blog/blog.html',{'posteos':posteos, 'categorias':categorias})


def categoria(request,categoria_id):
    
    categoria = Categoria.objects.get(id=categoria_id)
    posteos = Posteo.objects.filter(categorias=categoria)
    
    return render (request,'blog/categoria.html',{'posteos':posteos, 'categoria':categoria})

def post(request, slug_post):
    
    post = Posteo.objects.get(slug = slug_post)
    
    return render (request, 'blog/post.html',{'posteo':post})