Programa de inventario Versión 1.0

Comentarios:

Base de datos de artículos de informática: productos_informatica.db

-------------------------------------------------------------------

Menu principal del programa y llamado a la función:

1 - Carga de productos => ingresoDatos()

2 - Modificación de productos por id => modificarProducto()
	Nota: permite modificar todos los campos del registro

3 - Eliminación de productos por id => eliminarProducto()

4 - Listado de productos => listadoGral()

5 - Reporte bajo stock => reporteBajoStock()

--------------------------------------------------------------------

Funciones auxiliares


	listarCategorias():

Obtiene como resultado una consulta de las categorías de a tabla de productos. Retorna una lista de categorías.

	imprimirCategorias(lista): 

Recibe una lista de categorías y las imprime aplicándoles formato.

	buscarProductoId(valor):

Busca en la base de datos un producto y retorna un lista con los valores del registro o vacío.

	consultasVariasArticulos(query):

Recibe el texto de una Query y devuelve los artículos que cumplen con esa condición, retorna una lista con todos los campos del registro o vacío.

	mostrarProducto(registro):

Recibe una lista con un producto y todos sus campos y los muestra en detalle.

	registrarCambio(valor, id_de_campo, id_del_producto):

Registra en la base de datos el nuevo valor del campo modificado.

	cabecera(mensaje_Titulo):

Imprime un modelo de cabecera, recibe la leyenda del titulo a mostrar, es adaptable para diferentes informes.

	listadoProductos(lista_de_articulos):

Imprime las líneas de productos aplicándoles un formato previo.

-----------------------------------------------------------------------

Modulos importados:

sqlite3: Manejo de base de datos
time: se utiliza la función time.sleep(segundos) para poder visualizar mensajes y listados.

------------------------------------------------------------------------

Inicialización: El programa lleva cargado la creación de una tabla "productos" con 20 artículos para poder hacer las pruebas. Si detecta que la base de datos "productos_informatica" no tiene dicha tabla la crea y agrega los datos. Esto lo hace por única vez.

	