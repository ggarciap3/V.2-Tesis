from django.contrib import admin
from .models import Categoria, Tipospq, Lista
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'estado')

class TipospqAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'restriciones', 'imagen', 'estado')   #'precio', 'capacidad','indumentaria','recomendaciones', 'equipo_incluido'
    
class ListaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'cedula', 'email', 'telefono', 'fecha_creacion', 'fecha_compra', 'cantidad', 'Presentaciones', 'Productos', 'estado')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tipospq, TipospqAdmin)
admin.site.register(Lista, ListaAdmin)