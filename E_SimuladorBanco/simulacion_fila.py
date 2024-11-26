from ejemplo_uso import cuentas

def mostrar_menu():
    print("\nBienvenido al Banco")
    print("1. Seleccionar cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Consultar saldo")
    print("5. Salir")

def seleccionar_cuenta():
    print("\nSeleccione una cuenta:")
    for i, cuenta in enumerate(cuentas):
        print(f"{i + 1}. Cuenta {cuenta.numero_cuenta}")
    seleccion = int(input("Ingrese el número de la cuenta: ")) - 1
    return cuentas[seleccion]

def realizar_operacion(cuenta):
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            cuenta = seleccionar_cuenta()
        elif opcion == 2:
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == 3:
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == 4:
            cuenta.consultar_saldo()
        elif opcion == 5:
            print("Gracias por usar el Banco. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Iniciar la interfaz de usuario
cuenta_seleccionada = seleccionar_cuenta()
realizar_operacion(cuenta_seleccionada)
