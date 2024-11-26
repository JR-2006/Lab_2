import os
os.system('cls')

from logs import funcionLogs
from processUsuarios import procesarUsuarios, contarNumAccesos, imprimirResultados

def mostrar_menu():
    '''
    Muestra el menu principal para el usuario
    '''
    
    print("\nMenú de opciones:")
    print("1. Procesar los usuarios y contar accesos")
    print("2. Mostrar resultados de accesos")
    print("3. Salir")

def menu():
    '''
    Funcion del menu principal
    '''

    usuariosProcesados = []
    resultados = []
    
    while True:
        mostrar_menu()
        opcion = input("Elija una opción (1-3): ")
        
        if opcion == '1':
            # Obtener los logs y procesar los usuarios
            logs = funcionLogs()  # Llamamos a la función que retorna los logs
            usuariosProcesados = procesarUsuarios(logs)
            resultados = contarNumAccesos(usuariosProcesados)
            print("\nDatos procesados con éxito.")
        
        elif opcion == '2':
            # Mostrar resultados de accesos
            if resultados:
                imprimirResultados(resultados)
            else:
                print("\nPrimero debe procesar los datos (opción 1).")
        
        elif opcion == '3':
            # Salir del programa
            print("Hasta pronto.")
            break
        
        else:
            print("\nOpción no válida. Por favor, elija una opción entre 1 y 3.")

# Llamar a menu
if __name__ == "__main__":
    menu()
