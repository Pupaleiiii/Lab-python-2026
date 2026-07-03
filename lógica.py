from typing import TextIO

class Producto:
    cod_barras: str
    nombre: str
    categoria: str
    precio: float
    stock: int

class ItemCarrito:
    producto: Producto
    cantidad: int

def guardar_producto(producto: Producto):

    with open("productos.txt", "a") as archivo:
        escribir_producto(archivo, producto)

def leer_producto(linea: str):

    cod_barras, nombre, categoria, precio, stock = linea.strip().split(",")

    p = Producto()
    p.cod_barras = cod_barras
    p.nombre = nombre
    p.categoria = categoria
    p.precio = float(precio)
    p.stock = int(stock)

    return p

def escribir_producto(archivo: TextIO, producto_ingresado: Producto):
    
    archivo.write(
        f"{producto_ingresado.cod_barras},"
        f"{producto_ingresado.nombre},"
        f"{producto_ingresado.categoria},"
        f"{producto_ingresado.precio},"
        f"{producto_ingresado.stock}\n"
    )

def buscar_producto(cod_barras: str):
    
    with open("productos.txt", "r") as archivo:
        
        for linea in archivo:
            
            p = leer_producto(linea)
            
            if p.cod_barras == cod_barras:
                return p
    
    return None

def agregar_al_carrito(carrito: list[ItemCarrito], producto: Producto, cantidad: int):

    item = ItemCarrito()
    item.producto = producto
    item.cantidad = cantidad
    carrito.append(item)

def generar_ticket(carrito: list[ItemCarrito], metodo_pago: str):

    print("\n====================================================================")
    print("                       TICKET DE COMPRA")
    print("====================================================================")
    
    print(f"{'Producto':<33}{'Cant.':<8}{'P. Unitario':<15}{'Importe':>10}")
    print("-" * 68)

    total = 0

    for item in carrito:

        importe = item.producto.precio * item.cantidad
        total += importe

        print(
            f"{item.producto.nombre:33}"
            f"{item.cantidad:<8}"
            f"${item.producto.precio:<14.2f}"
            f"${importe:>9.2f}"
        )

    print("-" * 68)

    if metodo_pago.lower() == "efectivo":

        descuento = total * 0.10
        total_final = total - descuento

        print(f"{'Subtotal:':<45}${total:>9.2f}")
        print(f"{'Descuento (10%):':<45}-${descuento:>8.2f}")
        print(f"{'TOTAL A PAGAR:':<45}${total_final:>9.2f}")

    else:

        print(f"{'TOTAL A PAGAR:':<45}${total:>9.2f}")

    print("=" * 68)

def actualizar_stock(carrito: list[ItemCarrito]):

    productos: list[Producto] = []

    with open("productos.txt", "r") as archivo:

        for linea in archivo:
            productos.append(leer_producto(linea))

    for producto in productos:

        for item in carrito:

            if producto.cod_barras == item.producto.cod_barras:
                producto.stock -= item.cantidad

    with open("productos.txt", "w") as archivo:

        for producto in productos:

            escribir_producto(archivo, producto)

def cargar_producto():

    p = Producto()
    p.cod_barras = input("Ingrese el código de barras del producto: ")
    p.nombre = input("Ingrese el nombre del producto: ")
    p.categoria = input("Ingrese la categoría del producto: ")
    p.precio = float(input("Ingrese el precio del producto: "))
    p.stock = int(input("Ingrese el stock del producto: "))

    return p