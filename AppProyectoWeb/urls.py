from django.urls import path

from AppProyectoWeb import views
from django.conf.urls.static import static
from django.conf import settings  #para utilizar las variables url


urlpatterns = [
    path('', views.home, name='Home'),
    path('tienda/', views.tienda, name='Tienda'),
    path('contacto/', views.contacto, name='Contacto'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #Se agrega un path con ruta statica definida en el archivo settings