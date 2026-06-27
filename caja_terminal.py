# Acá deberías importar las funciones de tu archivo principal (suponiendo que se llama app.py)
# from app import buscar_producto, generar_ticket, carrito
from app import buscar_producto, generar_ticket, carrito
def iniciar_caja():
    while True:
        print("\n--- SISTEMA DE CAJA ---")
        print("1. Escanear producto")
        print("2. Cobrar y emitir ticket")
        print("3. Salir del sistema")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            codigo = input("Ingrese el código de barras: ")
            
            # Usamos tu función de búsqueda exacta
            producto_encontrado = buscar_producto(codigo)
            
            if producto_encontrado is not None:
                # En tu código agregabas el objeto Producto directamente a la lista
                carrito.append(producto_encontrado)
                print(f"--> ¡Agregado! {producto_encontrado.nombre} - ${producto_encontrado.precio}")
            else:
                print("--> Error: Producto no encontrado en la base de datos.")
                
        elif opcion == "2":
            # Validamos que haya algo en el carrito antes de cobrar
            if len(carrito) == 0:
                print("--> El carrito está vacío. Escanee un producto primero.")
                continue
                
            print("\n¿Cuál es el método de pago?")
            print("A - Efectivo (10% de descuento)")
            print("B - Tarjeta / Débito / Otros")
            
            opcion_pago = input("Seleccione método (A o B): ").lower()
            
            if opcion_pago == "a":
                metodo = "efectivo"
            else:
                metodo = "tarjeta"
                
            # Llamamos a la función de tu código principal para imprimir
            generar_ticket(carrito, metodo)
            
            # Vaciamos la lista del carrito para atender al siguiente cliente
            carrito.clear()
            
        elif opcion == "3":
            print("Cerrando la caja... ¡Hasta luego!")
            break
            
        else:
            print("--> Opción incorrecta, intente nuevamente.")

# Ejecutamos el menú del cajero
iniciar_caja()