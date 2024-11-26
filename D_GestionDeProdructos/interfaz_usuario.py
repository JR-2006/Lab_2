from inventario import mostrar_inventario
from ejemplo_uso import productos_inventario
from agregar_producto import agregar_producto

def mostrar_menu():
    print("\nSistema de Gestión de Productos")
    print("1. Mostrar inventario")
    print("2. Aumentar stock")
    print("3. Disminuir stock")
    print("4. Agregar nuevo producto")
    print("5. Salir")

def seleccionar_producto():
    print("\nSeleccione un producto:")
    for i, producto in enumerate(productos_inventario):
        print(f"{i + 1}. {producto.nombre}")
    seleccion = int(input("Ingrese el número del producto: ")) - 1
    return productos_inventario[seleccion]

def realizar_operacion():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            mostrar_inventario(productos_inventario)
        elif opcion == 2:
            producto = seleccionar_producto()
            cantidad = int(input("Ingrese la cantidad a aumentar: "))
            producto.aumentar_stock(cantidad)
        elif opcion == 3:
            producto = seleccionar_producto()
            cantidad = int(input("Ingrese la cantidad a disminuir: "))
            producto.disminuir_stock(cantidad)
        elif opcion == 4:
            agregar_producto(productos_inventario)
        elif opcion == 5:
            print("Gracias por usar el Sistema de Gestión de Productos. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Iniciar la interfaz de usuario
realizar_operacion()
