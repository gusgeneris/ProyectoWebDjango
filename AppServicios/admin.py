from django.contrib import admin
from .models import Servicios

# Register your models here.

class ModelServicios(admin.ModelAdmin): #Se solicita que muestre los campos created y update en el panel de administracion
    readonly_fields =('update','created') #se especifica que los campos sean de solo lectura

admin.site.register(Servicios,ModelServicios)