import json

#Crear la clase Producto
class Producto:
    def __init__ (self, nombre, precio, cantidad): #__init__ es el contructor de una clase
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad

    def __str__(self): #__str__ metodo especial para representar un objeto en cadena de texto
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"
    
#Crear las funciones
def agregar_producto(inventario, nombre, precio, cantidad): #Crear la funcion para agregar un producto al inventario
    for producto in inventario: #Recorrer cada producto del inventario
        if producto.nombre == nombre: #Si el producto ya esta en el inventario mostrar el mensaje y devolver el inventario
            print("El producto ya esta en el inventario")
            return inventario
    producto = Producto(nombre, precio, cantidad) #Si no esta en el inventario se crea ese producto
    inventario.append(producto) #Se añade ese producto al inventario
    return inventario

def procesar_pedido (pedidos, producto, cantidad): #Crear la funcion para procesar un pedido que se haga
    if producto.cantidad >= cantidad: #Si el producto que hay en la tienda es mayor o igual que el pedido
        producto.cantidad -= cantidad #Resta la cantidad pedida a lo que hay en tienda
        pedidos.append({"producto": producto.nombre, "cantidad": producto.cantidad}) #Se agrega un nuevo pedido a la lista de pedidos
        return True #Devuelve verdadero si el pedido se ha hecho con exito
    else:
        return False #Devuelve False si no se ha hecho el pedido con exito

def buscar_cliente (clientes, nombre):
    for cliente in clientes: #Recorrer cada cliente en la lista de clientes
        if cliente["nombre"] == nombre: #Si el nombre del cliente esta en la lista lo devuelve
            return cliente
        return None #Si no está se muestra none

def cargar_datos(archivo): #Pide el archivo json para abrirlo
    try:
        with open(archivo, "r") as f: #Se abre el archivo json en modo lectura
            return json.load(f) #Se utiliza la funcion json.load para cargar los datos en una variable (f)
    except FileNotFoundError: #Si hay un error devuelve el objeto vacio con las claves
        return{"inventario": [], "pedidos": [], "clientes": []}
       
               
def guardar_datos (archivo, datos): #Guardar los datos en el json
    with open(archivo, "w") as f: #Abrir el archivo en modo escritura (w) se asigna a la variable f
        json.dump(datos, f, indent=4) #Convetir a cada de texto los datos y el indent=4 es el numero para la cantidad de espacios que se van a utilizar

# Carga de datos desde archivo
datos = cargar_datos("datos.json")

inventario = datos["inventario"]
pedidos = datos["pedidos"]
clientes = datos["clientes"]

# Menú principal
while True: #Mostrar el menu
    print("Menú:")
    print("1. Agregar producto al inventario")
    print("2. Procesar pedido")
    print("3. Buscar cliente")
    print("4. Ver historial de pedidos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ") #Pedir la opcion por teclado

    if opcion == "1": #Si la opcion es 1
        #Pedir los datos del producto
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        inventario = agregar_producto(inventario, nombre, precio, cantidad) #Llamar a la funcion agragar producto y pasarle los datos introducidos
        print("Producto agregado")

    elif opcion == "2": #Si la opcion es 2
        #Pedir los datos
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        for producto in inventario: #Recorrer los productos del inventario
            if producto.nombre == nombre_producto: #Si el producto introducido esta en el inventario
                if procesar_pedido(pedidos, producto, cantidad): #Llama a la funcion procesar_pedido en un if
                    print("Pedido procesado") #Si hay suficiente cantidad se muestra el mensaje de pedido procesado
                else:
                    print("No hay suficiente stock del producto.") #Si no hay suficiente cantidad de producto se muestra el mensaje
                break
        else:
            print("Producto no encontrado.") #Si no hay ese producto se muestra este mensaje

    elif opcion == "3": #Si la opcion es 3
        nombre = input("Ingrese el nombre: ") #Pedir al usuario que introduzca el nombre que quiere buscar
        cliente = buscar_cliente(clientes, nombre) #Llama a la funcion cliente pasanadole el nombre a buscar y la lista de clients
        if cliente: #Si devuelve el cliente 
            print("Cliente encontrado:") #Muestra el cliente 
            print(f"Nombre: {cliente['nombre']}")
        else:
            print("Cliente no encontrado.") #Si no lo encuentra muestra el mensaje

    elif opcion == "4": #Si la opcion es 4
        print("Historial de pedidos:")
        for pedido in pedidos: #Recorre los pedidos en la lista de pedidos
            print(f"Producto: {pedido['producto']}, Cantidad: {pedido['cantidad']}") #Muestra los datos de los pedidos

    elif opcion == "5": #Si la opcion es 5 sale de la aplicacion
        break

    else:
        print("Opción inválida.") #Si no se introduce una opcion del 1 al 5 se mustra el mensaje de error

# Guarda los datos en el archivo
datos = {
    "inventario": [producto.__dict__ for producto in inventario], #Seutiliza dict para acceder a los atributos como un diccionario se asignan las clabes pedidos y clientes a las listas pedidos y clientes
    "pedidos": pedidos,
    "clientes": clientes}
guardar_datos("datos.json", datos)
