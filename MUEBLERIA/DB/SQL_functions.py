import mysql.connector
import datetime

#mysql -h bm9h8scsip6va76legry-mysql.services.clever-cloud.com -P 3306 -u uejpo6trlzp13yjr -p bm9h8scsip6va76legry
#Password: HMEJGv7Bs2rMQ8LCQZrj
def Abrir_Conexion():

	return mysql.connector.connect(
		#host="bm9h8scsip6va76legry-mysql.services.clever-cloud.com",
		host="DiegoC14062000.mysql.pythonanywhere-services.com",
		#password="HMEJGv7Bs2rMQ8LCQZrj",
		password="ben10pedro",
		#user="uejpo6trlzp13yjr",
		user="DiegoC14062000",
		port="3306",
		#db="bm9h8scsip6va76legry"
		db="DiegoC14062000$DB_Muebleria"
		) #Retorna la conexion establecida

def Cerrar_Conexion( sql ):
	sql.close()

def Ver_Tablas_de_DB( sql ):
	# sql: mysql.cursor -> Siendo mysql la conexion con DB [primero>Abrir_Conexion()]
	# -->> Retorna un lista con el nombre de todas las tablas de DB
	cur = sql.cursor()
	cur.execute("SHOW TABLES;")

	Tablas = []
	for campo in cur.fetchall():
		Tablas.append(campo[0])
	return Tablas

def Ver_Tabla( sql , Nombre_Tabla ):
	# sql: mysql.cursor -> Siendo mysql la conexion con DB [primero>Abrir_Conexion()]
	# Nombre_Tabla: Nombre de la Tabla a ver
	# -->> Retorna una tupla con todas las filas de DB

	cur = sql.cursor()
	Nombres_Campos_Tabla = Ver_Nombres_Campos_Tabla( sql , Nombre_Tabla )

	cur.execute("SELECT * FROM " + Nombre_Tabla)

	return genera_Diccionario_Campo_Valor( Nombres_Campos_Tabla , cur.fetchall() )

def genera_Diccionario_Campo_Valor( Array_Campos , Array_Registros ):
	# Dato un array de campos de una tabla y un array que contiene dentro arrays de registro de la misma tabla retornamos
	# por cada registro un diccionario [ { Campo: valor_registro ,...} , {....} , {....} ]
	# Array_Campos: Campos de la tabla
	# Array_Registros: array de Registros de la tabla [ [R1],[R2] .... ]

	Tabla = []
	for Registro in Array_Registros :
		Diccionario = {}
		for x in range( len( Array_Campos ) ):
			Diccionario[ Array_Campos[x] ] = Registro[x]
		Tabla.append( Diccionario )
	return Tabla

def Ver_Campos_y_Atributos_Tabla( sql , Nombre_Tabla ):
	# Retorna los campos de la Tabla
	# sql: mysql.cursor -> Siendo mysql la conexion con DB [primero>Abrir_Conexion()]
	# Nombre_Tabla: Nombre de la Tabla a ver DESCRIPCION
	# -->> Retorna una lista con todas las filas de DB
	cur = sql.cursor()
	cur.execute("DESCRIBE " + Nombre_Tabla)
	return( cur.fetchall() ) #Retorna una lista con todos los Campos de DB

def Ver_Nombres_Campos_Tabla( sql , Nombre_Tabla ):
	#Retorna lista con los nombres de los campos de la Tabla 'Nombre_Tabla'
	Campos_Tabla = Ver_Campos_y_Atributos_Tabla( sql , Nombre_Tabla )
	Nombres_Campo_Tabla = []
	for campo in Campos_Tabla:
		Nombres_Campo_Tabla.append( campo[0] )
	return Nombres_Campo_Tabla

def Insert_SQL( sql , Nombre_Tabla , Diccionario_Campos ):
	#sql: objeto con conexion establecida en DB
	#Nombre_Tabla: Nombre de la tabla a Insertar
	#Diccionario_Campos: Diccionario para ingresar a la Tabla
	cur = sql.cursor()

	Campos_Tabla = '('
	for Campo in Diccionario_Campos.keys():
		Campos_Tabla += Campo + ','
	Campos_Tabla = Campos_Tabla[0:len(Campos_Tabla)-1] + ')'

	cur.execute("INSERT INTO " + Nombre_Tabla + Campos_Tabla + " VALUES " + str( tuple(Diccionario_Campos.values()) )  )
	sql.commit() #Guardamos los cambios

#==============================================================>>>>>>>
#==============================================================>>>>>>>

def add_Categoria( Nombre , Nombre_Imagen , Description , Titulo_View ):
	SQL = Abrir_Conexion()

	Diccionario_New_Categoria = {
		'Nombre_Categoria': Nombre ,
		'Direccion_Imagen_Categoria': Nombre_Imagen ,
		'Descripcion_Categoria': Description ,
		'Titulo_Categoria': Titulo_View
	}
	Insert_SQL( SQL , 'categoriamueble' , Diccionario_New_Categoria )

	Cerrar_Conexion( SQL )

def add_Mueble(Nombre , Color , Categoria , Precio , Cantidad_Disponible , Porcentaje_Descuento , Descripcion_Corta , Descripcion_Larga , Array_Img ):

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
	= ingresomueble =
		+------------------+--------------+------+-----+---------+-------------------+
	| Field            | Type         | Null | Key | Default | Extra             |
	+------------------+--------------+------+-----+---------+-------------------+
	| Nombre_Mueble    | varchar(200) | NO   |     | NULL    |                   |
	| Color_Mueble     | varchar(100) | NO   |     | NULL    |                   |
	| Cantidad_Ingreso | int          | NO   |     | 0       | DEFAULT_GENERATED |
	| Fecha_Ingreso    | datetime     | NO   | PRI | NULL    |                  |
	+------------------+--------------+------+-----+---------+-------------------+
	'''

	SQL = Abrir_Conexion()

	#=====================>>>>
	#INGRESO DE MUEBLE NUEVO
	mueble_Campos = {
		'Nombre_Mueble': Nombre ,
		'Categoria_Mueble': Categoria ,
		'Precio_Mueble': Precio ,
		'Descuento_Mueble': Porcentaje_Descuento ,
		'Descripcion_Corta_Mueble': Descripcion_Corta ,
		'Descripcin_Larga_Mueble': Descripcion_Larga ,
		'Cantidad_Disponible_Mueble': Cantidad_Disponible
	}
	Insert_SQL( SQL , 'mueble' , mueble_Campos )
	#=====================>>>>

	#=====================>>>>
	#INGRESO DE IMAGENES DEL MUEBLE
	for Name_Img in Array_Img:
		Imagen_mueble_Campos = {
			'Nombre_Mueble': Nombre ,
			'Color_Mueble': Color ,
			'Direccion_Imagen_Mueble': Name_Img.name
		}
		Insert_SQL( SQL , 'imagenmueble' , Imagen_mueble_Campos )
	#=====================>>>>

	#=====================>>>>
	#INGRESO SU CAMPO A INGRESO, REGISTRO DE CAMBIO GENERADO
	ingresomueble_Campos = {
		'Nombre_Mueble': Nombre ,
		'Color_Mueble': Color ,
		'Cantidad_Ingreso': Cantidad_Disponible ,
		'Fecha_Ingreso': str( datetime.datetime.now() )
	}
	Insert_SQL( SQL , 'ingresomueble' , ingresomueble_Campos )
	#=====================>>>>

	Cerrar_Conexion( SQL )


def Buscar_Detalles_Producto( Nombre_Producto ):

	Nombres_Campos_Tabla = ['Nombre_Mueble','Categoria_Mueble','Precio_Mueble','Descuento_Mueble','Descripcion_Corta_Mueble','Descripcion_Larga_Mueble','Cantidad_Disponible_Mueble','Nombre_Mueble','Color_Mueble','Direccion_Imagen_Mueble']

	SQL = Abrir_Conexion()

	cur = SQL.cursor()
	cur.execute( "SELECT * FROM mueble INNER JOIN imagenmueble ON mueble.Nombre_Mueble = imagenmueble.Nombre_Mueble WHERE mueble.Nombre_Mueble LIKE '{}' ".format(Nombre_Producto) )
	resultados = cur.fetchall()

	Cerrar_Conexion( SQL )

	return genera_Diccionario_Campo_Valor( Nombres_Campos_Tabla , resultados )

def Buscar_Productos(Nombre_Producto):

	Nombres_Campos_Tabla = ['Nombre_Mueble','Categoria_Mueble','Precio_Mueble','Descuento_Mueble','Descripcion_Corta_Mueble','Descripcion_Larga_Mueble','Cantidad_Disponible_Mueble','Nombre_Mueble','Color_Mueble','Direccion_Imagen_Mueble']

	SQL = Abrir_Conexion()

	cur = SQL.cursor()

	cur.execute( "SELECT * FROM mueble INNER JOIN imagenmueble ON mueble.Nombre_Mueble = imagenmueble.Nombre_Mueble WHERE mueble.Nombre_Mueble LIKE '%{}%' ".format(Nombre_Producto) )

	resultados = cur.fetchall()

	Cerrar_Conexion( SQL )

	return genera_Diccionario_Campo_Valor( Nombres_Campos_Tabla , resultados )

#==============================================================>>>>>>>
#==============================================================>>>>>>>

#add_Categoria()
#SQL = Abrir_Conexion()
#print( Ver_Nombres_Campos_Tabla( SQL , 'Productos' ) )