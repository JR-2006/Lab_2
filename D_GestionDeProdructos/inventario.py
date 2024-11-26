from producto import Producto

def mostrar_inventario(productos):
    print("\nInventario de Productos:")
    for producto in productos:
        producto.mostrar_informacion()
