from django.db import models

#CharField es igual a VARCHAR segun documentacion de Django, requiere longitud
#TextField usado para ingrso de cadenas de textos gigantes


'''
#------------------- REGLAS GENERALES ----------------<<<>>>
#-----------------------------------------------------<<<>>>
	_ No esta permitido que ningun Nombre_Mueble tenga el simbolo '/'
#-----------------------------------------------------<<<>>>
#-----------------------------------------------------<<<>>>
'''

'''
Nombre_Mueble
Color_Mueble

Nombre_Categoria
'''
class update_imge(models.Model):
	Imagen = models.ImageField(null=True , upload_to='Carpeta_Imagenes/')

class categoriamueble(models.Model):

	Nombre_Categoria = models.CharField(max_length=100 , null=False , primary_key=True)
	Titulo_Categoria = models.CharField(max_length=100 , null=False)
	Descripcion_Categoria = models.CharField(max_length=200 , null=True)
	Dir_Img_Categoria = models.CharField(max_length=200,null=False,blank=True)

	Imagen = models.ImageField(null=True,upload_to ='DB/Imagenes')
    # Descuento_Categoria = models.CharField(max_length=100,null=False,default=0)
    # Sera parte de la Vista y contendra el descuento mas alto dentro de su categoria

class mueble(models.Model):
	Nombre_Mueble = models.CharField(max_length=200, null=False, primary_key=True)
	Categoria_Mueble = models.CharField(max_length=100, null=False)
	Precio_Muble = models.FloatField(null=False,default=0)
	Descuento_Mueble = models.IntegerField(null=False,default=0)
	Description_Corta_Mueble = models.CharField(max_length=300,null=False)
	Description_Larga_Mueble = models.CharField(max_length=600,null=False)
	Cantidad_Disponible_Muble = models.IntegerField(null=False,default=0)
	Color_Mueble = models.CharField(max_length=200,default='') #Al no encontrar el color indicado , toma el primero que encuentra disponible

	# El color no esta definido aca, el color tiene otra tabla donde defino imagenes
	# Todos los productos de igual nombre tienen el mismo precio

'''
class imagenmueble(models.Model):
	Nombre_Mueble = models.CharField(max_length=200, null=False)
	Color_Mueble = models.CharField(max_length=200,null=False)
	Dir_Img_Mueble = models.CharField(max_length=200,null=False)
'''
