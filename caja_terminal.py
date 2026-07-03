# Importamos las funciones de la lógica.py

from lógica import (
    ItemCarrito,
    guardar_producto,
    buscar_producto,
    agregar_al_carrito,
    cargar_producto,
    generar_ticket,
    actualizar_stock
)

def iniciar_caja():
    
    carrito: list[ItemCarrito] = []
    
    while True:
        print("\nSupermercado EL YACARÉ 2")
        print("1. Escanear producto")
        print("2. Cobrar y emitir ticket")
        print("3. Añadir producto nuevo a la base de datos")
        print("4. Salir del sistema")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            
            codigo = input("Escanee el producto o ingrese el código de barras: ")
            
            # Usamos la función de búsqueda para encontrar el producto
            producto_encontrado = buscar_producto(codigo)
            
            if producto_encontrado is not None:
                cantidad = int(input(f"¿Cuantas unidades de {producto_encontrado.nombre} desea agregar? "))
                agregar_al_carrito(carrito, producto_encontrado, cantidad)
                print(f"¡{producto_encontrado.nombre} - ${producto_encontrado.precio} x {cantidad} agregado exitosamente!")
            else:
                print("ERROR: Producto no encontrado en la base de datos.")
                
        elif opcion == "2":
            # Validamos que haya algo en el carrito antes de cobrar
            if len(carrito) == 0:
                print("ERROR: El carrito está vacío. Escanee un producto primero.")
                continue
                
            print("\n¿Cuál es el método de pago?")
            print("A - Efectivo (10% de descuento)")
            print("B - Tarjeta / Débito / Otros")
            
            opcion_pago = input("Seleccione método (A o B): ").lower()
            
            if opcion_pago == "a":
                metodo = "efectivo"
            else:
                metodo = "tarjeta"
                
            # Llamamos a la función para cobrar e imprimir ticket de compra
            generar_ticket(carrito, metodo)

            actualizar_stock(carrito)
            
            # Vaciamos la lista del carrito para dejarlo a disposición del siguiente cliente
            carrito.clear()
            
        elif opcion == "3":
            p = cargar_producto()
            guardar_producto(p)
        
        elif opcion == "4":
            print("Cerrando la caja... ¡Hasta luego!")
            break
            
        else:
            print("--> Opción incorrecta, intente nuevamente.")

# Ejecutamos el menú del cajero
iniciar_caja()