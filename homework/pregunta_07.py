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

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    contenido = __depurar_linea(PATH)

    repeticiones = {}
    for linea in contenido:
        valor = int(linea[1])
        if valor not in repeticiones:
            repeticiones[valor] = [linea[0]]
        else:
            repeticiones.get(valor).append(linea[0])
    return sorted(repeticiones.items())

print(pregunta_07())


