from producto import Producto

# Crear instancias de Producto
producto1 = Producto("Manzanas", 2000.0, 100)
producto2 = Producto("Naranjas", 1200.0, 80)
producto3 = Producto("Plátanos", 800.0, 150)

# Lista de productos
productos = [producto1, producto2, producto3]

# Simular operaciones de inventario
producto1.aumentar_stock(50)
producto2.disminuir_stock(30)
producto3.aumentar_stock(20)
producto3.disminuir_stock(50)

# Exportar la lista de productos para su uso en otras partes del programa
productos_inventario = productos
