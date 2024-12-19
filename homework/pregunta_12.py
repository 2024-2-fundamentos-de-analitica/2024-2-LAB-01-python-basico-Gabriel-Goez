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


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    contenido = __depurar_linea(PATH)

    resultado = {}
    for linea in contenido:
        quinta_columna = linea[4].split(",")
        letra = linea[0]
        for asociacion in quinta_columna:
            asociacion = asociacion.split(':')
            resultado[letra] = resultado.get(letra, 0) + int(asociacion[1])
            
    return resultado

    
print(pregunta_12())
