from webbrowser import register
from django.contrib import admin
from .models import Categoria, Posteo

# Register your models here.

class PosteoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Posteo,PosteoAdmin)