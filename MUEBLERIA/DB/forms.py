from django import forms
from .models import update_imge
from DB.SQL_functions import Abrir_Conexion , Cerrar_Conexion

# forms.ImageField(label='Imagen',widget=forms.ClearableFileInput(attrs={'multiple': True})) ===>>>> Multiples Imagenes Entrada

class Form_Entrada_Categorias(forms.Form):
	'''
	= categoriamueble = 
	+----------------------------+--------------+------+-----+---------+-------------------+
	| Nombre_Categoria           | varchar(100) | NO   | PRI | NULL
	| Direccion_Imagen_Categoria | varchar(200) | YES     
	| Descripcion_Categoria      | varchar(600) | NO       
	| Titulo_Categoria           | varchar(100) | YES  
	| Descuento_Categoria | int | YES
	+----------------------------+--------------+------+-----+---------+-------------------+
	'''
	
	Nombre_Categoria = forms.CharField(label='Nombre Categoria', max_length=90)
	Titulo_Categoria = forms.CharField(label='Titulo', max_length=90)
	Descripcion_Categoria = forms.CharField(label='Descripcion', max_length=560, widget=forms.Textarea())
	Imagen_Categoria = forms.ImageField(label='Imagen')

class Form_Entrada_Productos(forms.Form):
	''' 
	 = mueble = 
		+----------------------------+--------------+------+-----+---------+-------------------+
	| Field                      | Type         | Null | Key | Default | Extra             |
	+----------------------------+--------------+------+-----+---------+-------------------+
	| Nombre_Mueble              | varchar(200) | NO   | PRI | NULL    |                   |
	| Categoria_Mueble           | varchar(100) | NO   |     | NULL    |                   |
	| Precio_Mueble              | float        | NO   |     | 0       | DEFAULT_GENERATED |
	| Descuento_Mueble           | int          | NO   |     | 0       | DEFAULT_GENERATED |
	| Descripcion_Corta_Mueble   | varchar(300) | NO   |     | NULL    |                   |
	| Descripcin_Larga_Mueble    | varchar(600) | NO   |     | NULL    |                   |
	| Cantidad_Disponible_Mueble | int          | NO   |     | 0       | DEFAULT_GENERATED |
	+----------------------------+--------------+------+-----+---------+-------------------+
	'''
	
	'''
	= imagenmueble = 
		+-------------------------+--------------+------+-----+---------+-------+
	| Field                   | Type         | Null | Key | Default | Extra |
	+-------------------------+--------------+------+-----+---------+-------+
	| Nombre_Mueble           | varchar(200) | NO   |     | NULL    |       |
	| Color_Mueble            | varchar(100) | NO   |     | NULL    |       |
	| Direccion_Imagen_Mueble | varchar(200) | NO   |     | NULL    |       |
	+-------------------------+--------------+------+-----+---------+-------+
	'''

	'''
	Nombre
	Color
	Categoria
	Precio
	Cantidad Disponible 
	Descuento 
	Descripcion Corta
	Descripcion Larga
	Imagenes
	'''
	
	Nombre_Producto = forms.CharField(label='Nombre Producto', max_length=190)
	
	Opciones_Color = [
		('AZUL','AZUL'),
		('VERDE','VERDE'),
		('ROJO','ROJO'),
		('NEGRO','NEGRO'),
		('AMARILLO','AMARILLO'),
		('ROSA','ROSA'),
		('NARANJA','NARANJA'),
		('VIOLETA','VIOLETA'),
		('BLANCO','BLANCO'),
		('MARRON','MARRON'),
		('GRIS','GRIS'),
		]
	Color = forms.ChoiceField(label="Color" , choices=Opciones_Color)
	
	#===================>>>> Buscamos las Categorias Disponibles
	SQL = Abrir_Conexion()
	cur = SQL.cursor()
	cur.execute( "SELECT Nombre_Categoria FROM categoriamueble" )

	Categorias_Disponibles = []
	for Nombre_Categoria in cur.fetchall():
		print( 'Categoria: '+ Nombre_Categoria[0] )
		Categorias_Disponibles.append( ( Nombre_Categoria[0] , Nombre_Categoria[0] ) )
	Categoria = forms.ChoiceField(label="Nombre Categoria" , choices=Categorias_Disponibles)
	Cerrar_Conexion(SQL)
	#===================>>>>
	Precio = forms.FloatField(label='Precio' , min_value=0)
	
	Cantidad_Disponible = forms.IntegerField(label='Cantidad Disponible', min_value=0)
	
	Porcentaje_Descuento = forms.IntegerField(label='Porcentaje Descuento', min_value=0)
	
	Description_Corta = forms.CharField(label='Descripcion Corta', max_length=290, widget=forms.Textarea())
	
	Description_Larga = forms.CharField(label='Descripcion Larga', max_length=590, widget=forms.Textarea())
	
	Imagenes_Producto = forms.ImageField(label='Imagenes',widget=forms.ClearableFileInput(attrs={'multiple': True}))
	

class Form_Entrada_ImagenMueble(forms.Form):
	Imagenes_Producto = forms.ImageField( label='Imagenes', widget=forms.ClearableFileInput(attrs={'multiple': True}) )