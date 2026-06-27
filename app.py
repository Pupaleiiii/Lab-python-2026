class Producto:
    cod_barras: str
    nombre: str
    categoria: str
    precio: float
    stock: int

class ItemCarrito:
    producto: Producto
    cantidad: int

def cargar_producto(cod_barras_ingresado: str, nombre_ingresado: str, categoria_ingresada: str, precio_ingresado: float, stock_ingresado: int):
    
    p = Producto()
    p.cod_barras = cod_barras_ingresado
    p.nombre = nombre_ingresado
    p.categoria = categoria_ingresada
    p.precio = precio_ingresado
    p.stock = stock_ingresado

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{p.cod_barras},{p.nombre},{p.categoria},{p.precio},{p.stock}\n")

def buscar_producto(cod_barras: str):
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            cod_barras, nombre, categoria, precio, stock = linea.strip().split(",")
            if cod_barras == cod_barras:
                p = Producto()
                p.cod_barras = cod_barras
                p.nombre = nombre
                p.categoria = categoria
                p.precio = float(precio)
                p.stock = int(stock)
                return p
    return None

id_buscado = input("Escanee código de barras...")

producto_buscado = buscar_producto(id_buscado)

carrito = []

def agregar_al_carrito(carrito: list[ItemCarrito], producto: Producto, cantidad: int):

    item = ItemCarrito()
    item.producto = producto
    item.cantidad = cantidad
    carrito.append(item)


'''
cod_ingresado = input("Ingrese el código de barras del producto: ")
nombre_ingresado = input("Ingrese el nombre del producto: ")
categoria_ingresada = input("Ingrese la categoría del producto: ")
precio_ingresado = float(input("Ingrese el precio del producto: "))
stock_ingresado = int(input("Ingrese el stock del producto: "))

cargar_producto(cod_ingresado, nombre_ingresado, categoria_ingresada, precio_ingresado, stock_ingresado)
'''
