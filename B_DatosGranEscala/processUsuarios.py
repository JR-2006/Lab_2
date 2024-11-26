def procesarUsuarios(logs):
    '''
    Procesa los logs y extrae los usuarios
    '''

    usuariosProcesados = []
    for registro in logs:
        usuariosProcesados.append(registro["usuario"])
    return usuariosProcesados

def contarNumAccesos(usuariosProcesados):
    ''' 
    Cuenta cuántos accesos tiene cada usuario
    '''

    resultados = []
    usuarios_unicos = set(usuariosProcesados)
    for usuario in usuarios_unicos:
        numeroDeAccesos = usuariosProcesados.count(usuario)
        resultados.append([usuario, numeroDeAccesos])
    return resultados

def imprimirResultados(resultados):
    '''
    Imprime los resultados del conteo de accesos
    '''

    print("\nTotal de veces que usuarios ingresaron:")
    for resultado in resultados:
        print(f"Usuario: {resultado[0]}, Número de accesos: {resultado[1]}")
