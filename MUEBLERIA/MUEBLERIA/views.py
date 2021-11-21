

from django.shortcuts import render, redirect
from django.http import HttpResponse #Retornara datos JSON a la pagina

from DB.models import categoriamueble,mueble

import DB.forms

import DB.SQL_functions

import json

import MUEBLERIA.save_files

from pathlib import Path

'''
#------------------- REGLAS GENERALES ----------------<<<>>>
#-----------------------------------------------------<<<>>>
	_ No esta permitido que ningun Nombre_Mueble tenga el simbolo '/'
#-----------------------------------------------------<<<>>>
#-----------------------------------------------------<<<>>>
'''
BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
	#Prodria registrar la cantidad de gente que ingresa a la pagina contador
	#Solo se pasa una vez por este enlace y queda registrado , luego no existe forma
	return redirect('/Inicio') #Redirecciona  a la pagiana principal

def administrador_datos_mueble(request):
	if request.method == 'POST':

		formulario = DB.forms.Form_Entrada_Productos(request.POST,request.FILES)
		if formulario.is_valid():

			Imagenes_Productos = request.FILES.getlist('Imagenes_Producto')

			direccion_carpeta = str( BASE_DIR ) +'/MUEBLERIA/static/IMG_Proyecto'
			direccion_carpeta_Proyecto = 'MUEBLERIA/static/IMG_Proyecto'

			MUEBLERIA.save_files.Guardar_En_Carpeta_Django(direccion_carpeta_Proyecto,direccion_carpeta,Imagenes_Productos) #funcion en archivo: save_files.py

			Nombre = request.POST.get("Nombre_Producto")
			Color = request.POST.get("Color")
			Categoria = request.POST.get("Categoria")
			Precio = request.POST.get("Precio")
			Cantidad_Disponible = request.POST.get("Cantidad_Disponible")
			Porcentaje_Descuento = request.POST.get("Porcentaje_Descuento")
			Descripcion_Corta = request.POST.get("Description_Corta")
			Descripcion_Larga = request.POST.get("Description_Larga")

			#Guardamos los datos en DB
			DB.SQL_functions.add_Mueble( Nombre , Color , Categoria , Precio , Cantidad_Disponible , Porcentaje_Descuento , Descripcion_Corta , Descripcion_Larga , Imagenes_Productos )

	return render(request,'administrador_mueble.html',{"formulario": DB.forms.Form_Entrada_Productos() })

def administrador_datos_categoria(request):

	if request.method == 'POST':

		formulario = DB.forms.Form_Entrada_Categorias(request.POST,request.FILES)

		if formulario.is_valid():

			lista_imagenes = [request.FILES.get('Imagen_Categoria')] #En este caso solo llega 1 imagen

			direccion_carpeta = str( BASE_DIR ) + '/MUEBLERIA/static/IMG_Proyecto'
			direccion_carpeta_Proyecto = 'MUEBLERIA/static/IMG_Proyecto'

			MUEBLERIA.save_files.Guardar_En_Carpeta_Django(direccion_carpeta_Proyecto,direccion_carpeta,lista_imagenes) #funcion en archivo: save_files.py

			Nombre_Categoria = request.POST.get("Nombre_Categoria")
			Titulo_Categoria = request.POST.get("Titulo_Categoria")
			Description_Categoria = request.POST.get("Descripcion_Categoria")

			#Guardamos los datos en MysqlNombre_Categoria
			DB.SQL_functions.add_Categoria( Nombre_Categoria , lista_imagenes[0].name , Description_Categoria , Titulo_Categoria ) #funcion en archivo: DB.SQL_Function.add_Categoria_MYSQL

	return render(request,'administrador_categorias.html',{"formulario": DB.forms.Form_Entrada_Categorias()})



def addMueble(request):
	if request.method == 'POST': #Si se ingresan new Productos POST Django
		formulario = DB.forms.Form_Entrada_ImagenMueble(request.POST,request.FILES)
		if formulario.is_valid():

			Imagenes_Productos = request.FILES.getlist('Imagenes_Producto')
			direccion_carpeta = str( BASE_DIR ) +'\\MUEBLERIA\\static\\IMG_Proyecto'
			direccion_carpeta_Proyecto = 'MUEBLERIA/static/IMG_Proyecto'

			MUEBLERIA.save_files.Guardar_En_Carpeta_Django(direccion_carpeta_Proyecto,direccion_carpeta,Imagenes_Productos) #funcion en archivo: save_files.py

			print( request.POST.get("EntradaNombreMueble") )

	#GET
	return render(request,'admin_new_mueble.html',{"formularioImagen": DB.forms.Form_Entrada_ImagenMueble() })



def Inicio(request):
	return render(request,'index.html',{})

def Productos(request):

	SQL = DB.SQL_functions.Abrir_Conexion()

	Productos_Venta = DB.SQL_functions.Ver_Tabla( SQL , "productos_vista_html" ) #Llamamos a la vista ya creada

	DB.SQL_functions.Cerrar_Conexion( SQL )

	Productos_html = []
	Nombre_Anterior = "/"
	for producto in Productos_Venta:
		if producto['Nombre_Mueble'] != Nombre_Anterior:
			Nombre_Anterior = producto['Nombre_Mueble']
			Productos_html.append( producto )

	data = {
		'Productos' : Productos_html
	}

	return render(request,'productos.html',data)

def Detalles_Producto(request,Name_Product):

	Producto_detalles =  DB.SQL_functions.Buscar_Detalles_Producto( Name_Product )

	Direccion_Imagen_Mueble = []
	for Producto in Producto_detalles:
		Direccion_Imagen_Mueble.append( Producto["Direccion_Imagen_Mueble"] )

	Producto_detalles[0]["Direccion_Imagen_Mueble"] = Direccion_Imagen_Mueble #Contiene una lista de NOMBRE IMAGENES EN ESE CAMPO

	data = {
		'Producto' : Producto_detalles[0]
	}
	print( data )
	#'Nombre_Mueble','Categoria_Mueble','Precio_Mueble',
	#'Descuento_Mueble','Descripcion_Corta_Mueble','Descripcion_Larga_Mueble',
	#'Cantidad_Disponible_Mueble','Nombre_Mueble',
	#'Color_Mueble','Direccion_Imagen_Mueble'

	return render( request , 'detalle_producto.html' , data )

def Buscar_Productos(request):

	Nombre_Busqueda = request.GET.get('Producto_a_Buscar') #TRAE POR EL name

	data = {
		'Productos_Search' : DB.SQL_functions.Buscar_Productos( Nombre_Busqueda )
	}
	return HttpResponse(data['Productos_Search'])



