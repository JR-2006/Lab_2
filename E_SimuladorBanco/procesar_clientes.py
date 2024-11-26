from cuenta_bancaria import CuentaBancaria

def procesar_clientes(fila_clientes):
    while fila_clientes:
        cliente = fila_clientes.pop(0)
        print(f"Atendiendo al cliente con cuenta número: {cliente.numero_cuenta}")
        cliente.consultar_saldo()
