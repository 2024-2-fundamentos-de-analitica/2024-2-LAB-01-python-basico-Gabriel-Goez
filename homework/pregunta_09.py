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

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    contenido = __depurar_linea(PATH)
    repeticiones = {}
    for linea in contenido:
        clave_valor = linea[4].split(",")
        for asociacion in clave_valor:
            asociacion = asociacion.split(':')
            repeticiones[asociacion[0]] = repeticiones.get(asociacion[0], 0) + 1
    
    #return dict(sorted(repeticiones.items()))
    return dict(sorted(repeticiones.items()))


print(pregunta_09())
