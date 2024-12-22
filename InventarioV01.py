# Programa de inventario

# Importacion de librerias

import sqlite3
import time

# Inicializacion de base de datos

conexion = sqlite3.connect("productos_informatica.db")

cursor = conexion.cursor()

    # Creacion de base de datos

cursor.execute ('''
               CREATE TABLE IF NOT EXISTS "productos" (
	"id"	INTEGER NOT NULL,
	"descripcion"	VARCHAR(40),
	"cantidad"	INTEGER,
	"precio"	FLOAT,
	"categoria"	VARCHAR(40),
	PRIMARY KEY("id" AUTOINCREMENT)
);
                ''')

conexion.commit()

    # Verificacion de datos

cursor.execute("SELECT * FROM productos")

resultados = cursor.fetchall()

print(resultados)

if resultados == []:
    cursor.execute ('''
        INSERT INTO productos (descripcion, cantidad, precio, categoria) VALUES
        ('Laptop Dell', 10, 799.99, 'Computadoras'),
        ('Mouse Logitech', 50, 29.99, 'Periféricos'),
        ('Teclado Corsair', 30, 89.99, 'Periféricos'),
        ('Monitor Samsung', 20, 199.99, 'Pantallas'),
        ('SSD 1TB', 25, 129.99, 'Almacenamiento'),
        ('Placa de Video NVIDIA', 15, 499.99, 'Componentes'),
        ('Memoria RAM 16GB', 40, 79.99, 'Componentes'),
        ('Impresora HP', 5, 149.99, 'Impresión'),
        ('Router TP-Link', 60, 59.99, 'Redes'),
        ('Tarjeta Madre ASUS', 18, 129.99, 'Componentes'),
        ('Disco Duro 2TB', 22, 89.99, 'Almacenamiento'),
        ('Webcam Logitech', 12, 49.99, 'Periféricos'),
        ('Parlantes JBL', 25, 99.99, 'Audio'),
        ('Pendrive 64GB', 70, 19.99, 'Almacenamiento'),
        ('Cápsulas de aire aire acondicionado', 10, 15.99, 'Accesorios'),
        ('Cargador Universa', 8, 29.99, 'Accesorios'),
        ('Extensión Eléctrica', 40, 9.99, 'Accesorios'),
        ('Soporte para Monitor', 15, 39.99, 'Accesorios'),
        ('Kits de limpieza para computadora', 30, 14.99, 'Accesorios'),
        ('Cable HDMI', 50, 12.99, 'Accesorios');
                    ''')

    conexion.commit()


conexion.close()

### F U N C I O N E S  -  A U X I L I A R E S ###

    ## Imprime la lista de tuplas de categorias

def imprimirCategorias(lista):
    
    print("\n")

    for item in lista:
        print( f"{item[0]} - {item[1]} | ", end="" )


    ## Arma una lista con las categorias de productos

def listaCategorias():

    conexion = sqlite3.connect("productos_informatica.db")

    cursor = conexion.cursor()

    cursor.execute("SELECT DISTINCT categoria FROM productos")

    resultado = cursor.fetchall()

    listado = []
    contador = 1

    for dato in resultado:
        cat = dato[0]
        
        listado.append((contador,cat))
        contador += 1

    conexion.close()    
    
    return listado

    # Buscar un producto por ID

def buscarProductoId(indice):

    conexion = sqlite3.connect("productos_informatica.db")

    cursor = conexion.cursor()

    cursor.execute("SELECT *  FROM productos WHERE id=?",(indice,))

    resultado = cursor.fetchall()

    conexion.close()    
    
    return resultado

    # Ejecuta consultas de articulos sin restriccion de campos por distintos criterios que se pasan por parametro

def consultasVariasArticulos(consulta):

    conexion = sqlite3.connect("productos_informatica.db")

    cursor = conexion.cursor()

    cursor.execute(f"{consulta}")

    resultado = cursor.fetchall()

    conexion.close()    
    
    return resultado




    # Muestra el producto elegido desglozado por campos

def mostrarProducto(articulo):

    print("\n\t ID Seleccionado =>", articulo[0][0])
    print("\n\t 1 - Descripcion:",articulo[0][1])
    print("\n\t 2 - Cantidad:   ",articulo[0][2])
    print("\n\t 3 - Precio:     ",articulo[0][3])
    print("\n\t 4 - Categoria:  ",articulo[0][4])

def registrarCambio(dato,seleccion,id):

    confirma = input("\n\t Desea modificar el producto (s/n)")

    if confirma.upper() == "S":

        conexion = sqlite3.connect("productos_informatica.db")

        cursor = conexion.cursor()

        if seleccion == "1":

            cursor.execute("UPDATE productos SET descripcion = ?  WHERE id=?",(dato,id,))

        elif seleccion == "2":

            cursor.execute("UPDATE productos SET cantidad = ?  WHERE id=?",(dato,id,))
        
        elif seleccion == "3":

            cursor.execute("UPDATE productos SET precio = ?  WHERE id=?",(dato,id,))
        
        else:

            cursor.execute("UPDATE productos SET categoria = ?  WHERE id=?",(dato,id,))

        conexion.commit()
        conexion.close()    

        print("\n\t Producto modificado con exito!")
        cabecera("P R O D U C T O     M O D I F I C A D O")
        articuloMod = buscarProductoId(id)
        listadoProductos(articuloMod)
    else:
        print("\n\t Se cancelo la operacion!")
    
    time.sleep(3)

    # Imprime Cabecera

def cabecera(mensaje=""):
    print(f"\n\t\t\t\t {mensaje}")
    print(f"\n\t ID                 Descripcion              Stock       Precio         Categoria")

    # Listado de detalle de productos

def listadoProductos(articulo=[]):
    
    for dato in articulo:
        descripcionAcotada  = dato[1][:30]
        print(f"\n\t{dato[0]:2d}\t{descripcionAcotada:30}\t{dato[2]:10d}\t{dato[3]:10f}\t{dato[4]:20}")
    time.sleep(3)



### M E N U E S

    # Listado general de productos

def listadoGral():

    consulta = f"SELECT * FROM productos"

    resultado = consultasVariasArticulos(consulta)

    cabecera("L I S T A D O   G E N E R A L   P R O D U C T O S")
    listadoProductos(resultado)

    # Reporte bajo stock

def reporteBajoStock():

    limite = int(input("\n\t Indique por favor el stock minimo a considerar: "))

    consulta = f"SELECT * FROM productos WHERE cantidad <= {limite}"

    resultado = consultasVariasArticulos(consulta)

    if resultado == []:
        print("\n\t No hay articulos que cumplan con ese parametro")
        time.sleep(2)
        return

    cabecera(f"L I S T A D O   D E   B A J O   S T O C K - Cantidad limite: {limite}")

    listadoProductos(resultado)

    time.sleep(3)

    # Ingreso de datos

def ingresoDatos():
    # Solicitud de datos
    print("\n\t * INGRESO DE DATOS *")
    producto = input("\n\t Ingrese la descripcion del producto: ")
    cantidad = int(input("\n\t Ingrese la cantidad del producto: "))
    precio = float(input("\n\t Ingrese el precio del producto: "))

    # usa funciones auxiliares para elegir una categoria existente
    categorias = listaCategorias()
    imprimirCategorias(categorias)
    numCategoria = int(input("\n\t Ingrese una categoria del listado: "))
    categoriaElegida = categorias[numCategoria-1][1]

    # confirmacion de carga
    articulo = [(0, producto, cantidad, precio, categoriaElegida)]
    cabecera("A L T A   D E   P R O D U C T O")
    listadoProductos(articulo)
    confirma = input("\n\t Detalle del articulo a ingresar (Confirma s/n)")
    if confirma.upper() == "S":
        conexion = sqlite3.connect("productos_informatica.db")
        cursor = conexion.cursor()
        cursor.execute("""
        INSERT INTO productos (descripcion, cantidad, precio, categoria) VALUES 
        (?, ?, ?, ?)""", (producto, cantidad, precio, categoriaElegida))
        conexion.commit()
        conexion.close()
        print("\n\t Producto satisfactoriamente agregado!")
    else:
        print("\n\t Se cancelo la registracion")
    time.sleep(3)

    # Modificacion de datos

def modificarProducto():
    print("\n\t * MODIFICACION DE DATOS *")
    id = input("\n\t Ingrese el id del articulo a modificar: ")

    productoElegido = buscarProductoId(id)

    if productoElegido == []:
        print("\n\t No se encuentra el producto!")
        time.sleep(3)
        return

    mostrarProducto(productoElegido)

    seleccionado = "s"
    
    while seleccionado.upper() !="N":

        seleccionado = input("\n\tIndique el campo a modicar: ")

        if seleccionado == "1":
            nvaDescripcion = input("\n\t Ingrese la nueva descripcion: ")
            registrarCambio(nvaDescripcion,seleccionado,id)
            break
        elif seleccionado == "2":
            nvaCantidad = int(input("\n\t Ingrese la nueva cantidad: "))
            registrarCambio(nvaCantidad,seleccionado,id)
            break
        elif seleccionado == "3":
            nvoPrecio = float(input("\n\t Ingrese el nuevo precio: "))
            registrarCambio(nvoPrecio,seleccionado,id)
            break
        elif seleccionado == "4":
            categorias = listaCategorias()
            imprimirCategorias(categorias)
            numCategoria = int(input("\n\t Ingrese una categoria del listado: "))
            categoriaElegida = categorias[numCategoria-1][1]
            registrarCambio(categoriaElegida,seleccionado,id)
            break
        else:
            print("\n\t Ingrese un opcion valida o  'n' para salir")
            
    # Eliminacion de productos

def eliminarProducto():

    print("\n\t * ELIMINACION DE DATOS *")
    id = input("\n\t Ingrese el id del articulo a eliminar: ")

    productoElegido = buscarProductoId(id)

    if productoElegido == []:
        print("\n\t No se encuentra el producto!")
        time.sleep(3)
        return

    mostrarProducto(productoElegido)

    confirma = input("\n\t Desea eliminar el producto (s/n): ")

    if confirma.upper() == "S":
        conexion = sqlite3.connect("productos_informatica.db")
        cursor = conexion.cursor()
        cursor.execute("""
        DELETE FROM productos WHERE id = ?""", (id,))
        conexion.commit()
        conexion.close()
        print("\n\t Producto eliminado!")
    else:
        print("\n\t Se cancelo la operacion")
    time.sleep(3)

# Inicializacion de variables


opcion = "S"


# Menu principal

while opcion.upper() != "N":

    # Menu de opciones
    print("\n")
    print("\t", end = " ")
    print("#"*20)
    print("\t # MENU DE OPCIONES #")
    print("\t",end=" ")
    print("#"*20)
    print("\n")
    print("\t  1 : Carga de productos")
    print("\n\t  2 : Modificacion de productos por id")
    print("\n\t  3 : Eliminacion de productos por id")
    print("\n\t  4 : Listado de productos")
    print("\n\t  5 : Reporte bajo stock")
    print("\n\t  Pulse 'n' para salir")

    # Ingreso de opcion
    
    opcion = input("\n\t Ingrese una opcion del menu : ")

    # Seleccion de opciones

    if opcion == "1":

        ingresoDatos()
    
    elif opcion == "2":
        
        modificarProducto()

    elif opcion == "3":
        
        eliminarProducto()

        
    elif opcion == "4":
        
        listadoGral()

    elif opcion == "5":

        reporteBajoStock()

    elif opcion.upper() == "N":
        print("\n\t Gracias por usar nuestro sistema")
        break
    else:
        print("\n\t Ha elegido una opcion incorrecta!")


   