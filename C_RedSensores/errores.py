def errores(opcion, rango_valido):
    try:
        opcion = int(opcion)
        if opcion in rango_valido:
            return opcion
        else:
            print(f"Opción {opcion} no es válida. Debe estar dentro del rango {rango_valido}.")
            return None
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return None
