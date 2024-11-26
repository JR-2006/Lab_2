class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de {monto} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("El monto del depósito debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

    def consultar_saldo(self):
        print(f"El saldo de la cuenta {self.numero_cuenta} es: {self.saldo}")
        return self.saldo
