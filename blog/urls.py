from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings  #para utilizar las variables url donde se almacenaran las imagenes

urlpatterns=[
    path ('', views.blog, name='Blog'),
    path ('categoria/<int:categoria_id>',views.categoria, name='Categoria')
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #Se agrega un path con ruta statica definida en el archivo settings