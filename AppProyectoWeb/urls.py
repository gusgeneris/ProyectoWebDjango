from django.urls import path
from AppProyectoWeb import views


urlpatterns = [
    path('', views.home, name='Inicio'),
    path('servicios/', views.servicios),
    path('tienda/', views.tienda),
    path('blog/', views.blog),
    path('contacto/', views.contacto),
]