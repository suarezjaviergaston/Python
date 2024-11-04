# Programa de inventario

# Inicializacion de variables

producto = ""
cantidad = 0
precio = 0

item = []
bdProductos = []

continuar = "S"

# Bucle de carga de datos

while continuar.upper() != "N":

    # Menu de opciones
    print("\n")
    print("\t", end = " ")
    print("#"*20)
    print("\t # MENU DE OPCIONES #")
    print("\t",end=" ")
    print("#"*20)
    print("\n")
    print("\t  1 : Carga de datos")
    print("\n\t  2 : Mostrar datos cargados")
    print("\n\t  Pulse n para salir")

    # Ingreso de opcion
    
    continuar = input("\n\t Ingrese una opcion del menu : ")

    # Seleccion de opciones

    if continuar == "1":
        # Solicitud de datos
        print("\n\t * INGRESO DE DATOS *")
        producto = input("\n\t Ingrese el nombre del producto: ")
        cantidad = int(input("\n\t Ingrese la cantidad del producto: "))
        precio = float(input("\n\t Ingrese el precio del producto: "))
        # Creacion del item a agregar
        item = [producto.upper(),cantidad,precio]
        # Agrega el item a la base de datos
        bdProductos.append(item)

    elif continuar == "2":
        # Lista los datos
        # Cabecera del listado
        print("\n\t\t * LISTADO DE PRODUCTOS *")
        print(f"\t Articulo \t | Cantidad \t\t | Precio")
        print("\t", end=" ")
        print("-"*50)
        for item in bdProductos:
            #Verifica el largo de la cadena a imprimir para encuadrar mejor la salida de la informacion
            if len(item[0]) <= 6:
                print(f"\t {item[0]} \t\t\t {item[1]} \t\t {item[2]}")
            else:
                print(f"\t {item[0]} \t\t {item[1]} \t\t {item[2]}")

    elif continuar.upper() == "N":
        print("\n\t Gracias por usar nuestro sistema")
        break
    else:
        print("\n\t Ha elegido una opcion incorrecta!")


    