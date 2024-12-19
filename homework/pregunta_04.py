"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

PATH = 'files/input/data.csv'
def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    with open(PATH) as archivo: 
        contenido = archivo.read().splitlines()

    ocurrencia_mes = {}

    for linea in contenido:
        if linea.strip():
            fecha_str = linea.split('\t')[2]
            fecha_str = fecha_str.split('-')
            mes   = fecha_str[1]
            ocurrencia_mes[mes] = ocurrencia_mes.get(mes, 0) + 1

    return sorted(ocurrencia_mes.items()) 

print(pregunta_04())

