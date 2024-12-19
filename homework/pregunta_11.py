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


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    contenido = __depurar_linea(PATH)

    sumatoria = {}
    for linea in contenido:
        cuarta_columna = linea[3].split(',')

        for valor in cuarta_columna:

            sumatoria[valor] = sumatoria.get(valor, 0) + int(linea[1])

    return dict(sorted(sumatoria.items()))

print(pregunta_11())
    