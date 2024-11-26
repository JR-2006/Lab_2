class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def aumentar_stock(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se han añadido {cantidad} unidades de {self.nombre}. Nuevo stock: {self.cantidad}")
        else:
            print("La cantidad a aumentar debe ser positiva.")

    def disminuir_stock(self, cantidad):
        if 0 < cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}. Stock restante: {self.cantidad}")
        else:
            print("Cantidad insuficiente en stock o cantidad inválida.")

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")
