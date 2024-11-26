from producto import Producto

def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    nuevo_producto = Producto(nombre, precio, cantidad)
    productos.append(nuevo_producto)
    print(f"Producto {nombre} añadido al inventario.")
