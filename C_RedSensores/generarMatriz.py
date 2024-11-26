import random


def generateMatrizTemp(n, m):
    '''
    Generar matrices con valores aleatorios
    '''
    matrizTemp = []
    for i in range(n):
        fila = []
        for j in range(m):
            # Generar una temperatura aleatoria entre 0 y 100 grados Celsius
            temperatura = round(random.uniform(0, 100), 2)
            fila.append(temperatura)
        matrizTemp.append(fila)
    return matrizTemp
