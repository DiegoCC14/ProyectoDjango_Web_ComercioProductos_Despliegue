from django.contrib import admin

#from DB.models import *
from DB.forms import *


# Register your models here.

#list_editable = ['Descripcion_Categoria'] Se pueden modificar los campos tomados
#list_filter = ['Nombre_Categoria'] Muestra todos los titulos y filtra por esos valores
#search_fields = ['Nombre_Categoria'] Search por los Nombre_Categoria
#list_per_page = 2 Divide por paginas cada 2 elementos
#ordering = ["NombreColumnaOrden"]
#date_hierarchy = ["NombreCampoFecha"] / "NombreCampoFecha" Ingresa Filtro Fecha por anio

class Categoria_Mueble_Interface(admin.ModelAdmin):
	list_display = ['Nombre_Categoria','Titulo_Categoria','Descripcion_Categoria','Dir_Img_Categoria','Imagen']
	list_filter = ['Nombre_Categoria']

class Mueble_Interface(admin.ModelAdmin):
	list_display = ['Nombre_Mueble','Categoria_Mueble','Precio_Muble','Descuento_Mueble','Cantidad_Disponible_Muble','Description_Corta_Mueble']
	list_filter = ['Categoria_Mueble']
	search_fields = ['Nombre_Mueble']
	

#admin.site.register(categoriamueble,Categoria_Mueble_Interface)

#admin.site.register(mueble,Mueble_Interface)
