def solicitudCuadrado():
    return float(input("Digite el lado: "))

def solicitudTriangulo():
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    return base, altura

def solicitudCirculo():
    return float(input("Digite el radio: "))

def solicitudPentagono():
    perimetro = float(input("Digite el perimetro: "))
    apotema = float(input("Digite la apotema: "))
    return perimetro, apotema

def solicitudTrapecio():
    baseMayor = float(input("Digite la base mayor: "))
    baseMenor = float(input("Digite la base menor: "))
    altura = float(input("Digite la altura: "))
    return baseMayor, baseMenor, altura

def solicitudRomboide():
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    return base, altura

def solicitudRombo():
    diagonalMayor = float(input("Digite el diagonal mayor: "))
    diagonalMenor = float(input("Digite el diagonal menor: "))
    return diagonalMayor, diagonalMenor

def solicitudRectangulo():
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    return base, altura
