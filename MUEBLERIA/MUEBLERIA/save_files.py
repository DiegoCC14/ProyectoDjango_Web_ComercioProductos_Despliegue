
from django.core.files.storage import FileSystemStorage

import os

def Guardar_En_Carpeta_Django(Nombre_Carpeta_Proyecto_Django,Direccion_Carpeta,Array_Archivo): 
	#Nombre_Carpeta_Proyecto_Django: Indicamos la carpeta donde guardaremos el Archivo ejemplo: DB/IMG_Proyecto/  dentro del pryecto
	#Direccion_Carpeta: La direccion Compleeta de la carpeta donde guardaremos el Archivo
	#Archivo: Archivo que guardaremos que contiene el Nombre ===>>> JSON
	
	fs = FileSystemStorage( Nombre_Carpeta_Proyecto_Django ) #Solo sirve con DJANGO
	
	for Archivo in Array_Archivo:
		Nombre_Archivo_Sin_Extencion = get_name_file( Archivo.name )
		if Existe_Archivo_En_Carpeta(Direccion_Carpeta,Nombre_Archivo_Sin_Extencion) == False:
			fs.save(Archivo.name , Archivo) #Guardamos los archios en el caso de que no se encuentren


def Existe_Archivo_En_Carpeta(Direccion_Carpeta,Nombre_Archivo_Sin_Extencion):
	#Retorna True si Nombre_Archivo_Sin_Extencion se encuentra en Direccion_Carpeta
	lista_archivos = os.listdir(Direccion_Carpeta)
	lista_nombre_archivos = get_list_name_file(lista_archivos)
	return( lista_nombre_archivos.count(Nombre_Archivo_Sin_Extencion)>0 )

def get_list_name_file(Lista_Archivos):
	#Dada la lista de nombre de archivos retornamos lista con solo su nombre sin extencion 
	lista = []
	for archivo in Lista_Archivos:
		lista.append( get_name_file(archivo) )
	return(lista)

def get_name_file(Nombre_Archivo):
	#Dado el Nombre Archivo retorna su Nombre sin su Extencion
	for pos in range(len(Nombre_Archivo)-1,-1,-1):
		if(Nombre_Archivo[pos]) == '.':
			return( Nombre_Archivo[0:pos] )
	return('NO SE TRATA DE UN ARCHIVO CON EXTENCION, PUEDE SER UNA CARPETA (def Nombre_Archivo)')

#Direccion_Carpeta = 'E:\\Proyectos_Django_2021\\PROYECTO_COMERCIO_MUEBLES\\MUEBLERIA\\DB\\IMG_Proyecto\\'
#print( Existe_Archivo_En_Carpeta(Direccion_Carpeta ,'Shreck') )

#Guardar_En_Carpeta_Django('Nombre_Carpeta_Proyecto_Django',Direccion_Carpeta,[],[])