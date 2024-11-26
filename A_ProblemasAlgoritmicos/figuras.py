import math

def areaCuadrado(lado):
    return lado * lado

def areaTriangulo(base, altura):
    return (base * altura) / 2

def areaCirculo(radio):
    return radio * radio * math.pi

def areaPentagono(perimetro, apotema):
    return (perimetro * apotema) / 2

def areaTrapecio(baseMayor, baseMenor, altura):
    return ((baseMayor + baseMenor) / 2) * altura

def areaRomboide(base, altura):
    return base * altura

def areaRombo(diagonalMayor, diagonalMenor):
    return (diagonalMayor * diagonalMenor) / 2

def areaRectangulo(base, altura):
    return base * altura
