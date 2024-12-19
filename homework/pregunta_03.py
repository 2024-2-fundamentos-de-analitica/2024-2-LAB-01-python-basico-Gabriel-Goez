"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

PATH = 'files/input/data.csv'
def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open(PATH) as archivo:
        contenido = archivo.readlines()
    sumatoria_letra = {}
    for linea in contenido:
    
        if linea.strip():
            linea_depurada = linea.split('\t')
            letra = linea_depurada[0]
            valor = int(linea_depurada[1])
            sumatoria_letra[letra] = sumatoria_letra.get(letra, 0) + valor

    return sorted(sumatoria_letra.items()) 

print(pregunta_03())