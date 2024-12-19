"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

PATH = 'files/input/data.csv'

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    with open(PATH) as archivo:
        contenido = archivo.read().splitlines()
    
    diccionario = {}
    for linea in contenido:
        if linea.strip():
            linea_depurada = linea.split('\t')
            lista_diccionarios = linea_depurada[4].split(',')
            for clave_valor in lista_diccionarios:
                clave_valor = clave_valor.split(':')
                clave = clave_valor[0]
                valor = int(clave_valor[1])
                
                if clave not in diccionario:
                    diccionario[clave] = {'max': valor, 'min': valor}
                else:
                    diccionario[clave]['max'] = max(diccionario[clave]['max'], valor)
                    diccionario[clave]['min'] = min(diccionario[clave]['min'], valor)
            
    
    resultado = []
    for i in sorted(diccionario.items()):
        clave_dict = i[0]
        clave_max = i[1]['max']
        clave_min = i[1]['min']
        resultado.append((clave_dict, clave_min, clave_max))

    return resultado

