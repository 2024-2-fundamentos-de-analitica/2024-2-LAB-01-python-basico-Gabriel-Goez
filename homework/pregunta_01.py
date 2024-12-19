"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    with open('files/input/data.csv', 'r') as archivo:
        contenido = archivo.read()

    # Procesar cada línea del contenido
    contenido = contenido.split("\n")
    # Inicializar la suma
    suma = 0
    for line in contenido[:-1]:  # Dividir en líneas
    
        columns = line.split("\t")  # Dividir la línea en columnas usando tabulación
        
        suma += int(columns[1])  # Convertir la segunda columna a entero y sumar
    return suma

       