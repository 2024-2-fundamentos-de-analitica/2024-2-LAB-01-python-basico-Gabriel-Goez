"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    # """
    # Abrir y leer el archivo
    with open('files/input/data.csv', 'r') as archivo:
        contenido = archivo.readlines()  # Leer todas las líneas del archivo

    # Crear un diccionario para contar las ocurrencias de cada letra
    conteo = {}
    for linea in contenido:
        if linea.strip():  # Ignorar líneas vacías
            letra = linea.split("\t")[0]  # Extraer la letra de la primera columna
            conteo[letra] = conteo.get(letra, 0) + 1  # Incrementar el conteo

    # Convertir el diccionario a una lista de tuplas ordenadas alfabéticamente
    resultado = sorted(conteo.items())

    return resultado

print(pregunta_02())