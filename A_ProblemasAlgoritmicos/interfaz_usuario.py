from figuras import *
from solicitud_datos import *
from mostrar_resultados import mostrarResultado

def menu():
    print("\nBienvenido a la calculadora de figuras")
    print("1. Cuadrado")
    print("2. Triangulo")
    print("3. Circulo")
    print("4. Pentagono")
    print("5. Trapecio")
    print("6. Romboide")
    print("7. Rombo")
    print("8. Rectangulo")
    print("9. Salir")
    return int(input("Digite una opción del menú: "))

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            lado = solicitudCuadrado()
            area = areaCuadrado(lado)
            mostrarResultado("cuadrado", area)
        elif opcion == 2:
            base, altura = solicitudTriangulo()
            area = areaTriangulo(base, altura)
            mostrarResultado("triángulo", area)
        elif opcion == 3:
            radio = solicitudCirculo()
            area = areaCirculo(radio)
            mostrarResultado("círculo", area)
        elif opcion == 4:
            perimetro, apotema = solicitudPentagono()
            area = areaPentagono(perimetro, apotema)
            mostrarResultado("pentágono", area)
        elif opcion == 5:
            baseMayor, baseMenor, altura = solicitudTrapecio()
            area = areaTrapecio(baseMayor, baseMenor, altura)
            mostrarResultado("trapecio", area)
        elif opcion == 6:
            base, altura = solicitudRomboide()
            area = areaRomboide(base, altura)
            mostrarResultado("romboide", area)
        elif opcion == 7:
            diagonalMayor, diagonalMenor = solicitudRombo()
            area = areaRombo(diagonalMayor, diagonalMenor)
            mostrarResultado("rombo", area)
        elif opcion == 8:
            base, altura = solicitudRectangulo()
            area = areaRectangulo(base, altura)
            mostrarResultado("rectángulo", area)
        elif opcion == 9:
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción inválida...")

if __name__ == "__main__":
    main()
