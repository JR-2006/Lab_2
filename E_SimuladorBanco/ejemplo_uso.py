from cuenta_bancaria import CuentaBancaria

# Ejemplo de uso
cuenta1 = CuentaBancaria("001", 1000)
cuenta2 = CuentaBancaria("002", 500)

cuenta1.depositar(200)
cuenta1.retirar(150)
cuenta1.consultar_saldo()

cuenta2.depositar(300)
cuenta2.retirar(100)
cuenta2.consultar_saldo()

# Exportar las cuentas para su uso en otras partes del programa
cuentas = [cuenta1, cuenta2]
