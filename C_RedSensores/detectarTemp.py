def clasificarTemperaturas(matrizTemp):
    ''''
    Clasificacion de las temperaturas
        *Criticas
        *Altisimas
        *Altas
        *Normales
        *Frias
    '''
    categorias = {
        "Temperaturas Críticas (superior a 80°C)": [],
        "Temperaturas Altísimas (superior a 60°C)": [],
        "Temperaturas Altas (superior a 40°C)": [],
        "Temperaturas Normales (15 a 40°C)": [],
        "Temperaturas Frías (inferior a 15°C)": []
        }
    
    for i in range(len(matrizTemp)):
        for j in range(len(matrizTemp[i])):
            temp = matrizTemp[i][j]
            if temp > 80:
                categorias["Temperaturas Críticas (superior a 80°C)"].append((i, j, temp))
            elif temp > 60:
                categorias["Temperaturas Altísimas (superior a 60°C)"].append((i, j, temp))
            elif temp > 40:
                categorias["Temperaturas Altas (superior a 40°C)"].append((i, j, temp))
            elif temp >= 15:
                categorias["Temperaturas Normales (15 a 40°C)"].append((i, j, temp))
            else:
                categorias["Temperaturas Frías (inferior a 15°C)"].append((i, j, temp))
    return categorias
