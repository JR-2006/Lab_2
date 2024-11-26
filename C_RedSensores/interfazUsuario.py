from generarMatriz import generateMatrizTemp
from detectarTemp import clasificarTemperaturas
from errores import errores

import os
os.system('cls')

print("Bienvenido a la Simulacion de red de sensores de Temperatura\n")


def menuPrincipal():
    '''
    Menu principal
    '''
    print("\n--- Menú de Opciones ---")
    print("1. Generar matriz de temperaturas")
    print("2. Detectar y clasificar temperaturas")
    print("3. Mostrar matriz de temperaturas")
    print("4. Salir")
    opcion = input("Por favor, seleccione una de las opciones: ")
    return opcion

# Dimensiones de la matriz
n = 5  # número de filas
m = 5  # número de columnas

# Inicializar la matriz de temperaturas
matriz_temperaturas = []

rango_valido = range(1, 5)

while True:
    opcion = menuPrincipal()
    opcion_valida = errores(opcion, rango_valido)
    
    if opcion_valida == 1:
        # Generar la matriz de temperaturas
        matriz_temperaturas = generateMatrizTemp(n, m)
        print("\nMatriz de temperaturas generada.\n\n")
    
    elif opcion_valida == 2:
        if matriz_temperaturas:
            # Detectar y clasificar temperaturas
            categorias_temperaturas = clasificarTemperaturas(matriz_temperaturas)
            print("\nClasificación de temperaturas:")
            for categoria, temperaturas in categorias_temperaturas.items():
                print(f"\n{categoria}:")
                for temp in temperaturas:
                    print(f"  Posición: ({temp[0]}, {temp[1]}), Temperatura: {temp[2]}°C")
        else:
            print("Primero debes generar la matriz de temperaturas (opción 1).")
    
    elif opcion_valida == 3:
        if matriz_temperaturas:
            # Mostrar la matriz de temperaturas
            print("\nMatriz de temperaturas:")
            for fila in matriz_temperaturas:
                print(fila)
        else:
            print("Primero debes generar la matriz de temperaturas (opción 1).")
    
    elif opcion_valida == 4:
        # Salir del programa
        print("Saliendo de la simulación del programa...")
        break
