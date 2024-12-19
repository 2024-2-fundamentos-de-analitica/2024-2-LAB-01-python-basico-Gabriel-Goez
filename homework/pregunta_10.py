"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

PATH = 'files/input/data.csv'
def __depurar_linea(path):
    
    with open(path) as archivo:
        contenido = archivo.read().splitlines()
    
    linea_depurada = []
    for linea in contenido:
        if linea.strip():
            linea = linea.split('\t')

            linea_depurada.append(linea)

    return linea_depurada


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    contenido = __depurar_linea(PATH)

    respuesta = []
    for linea in contenido:
        cuarta_columna = len(linea[3].split(","))
        quinta_columna = len(linea[4].split(","))
        letra          = linea[0]
        respuesta.append((letra, cuarta_columna, quinta_columna))
    return respuesta

print(pregunta_10())
