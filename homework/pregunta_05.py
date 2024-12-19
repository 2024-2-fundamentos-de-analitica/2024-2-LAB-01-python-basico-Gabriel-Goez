"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
PATH = 'files/input/data.csv'

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open(PATH) as archivo:
        contenido = archivo.read().splitlines()
        
    max_min = {}

    for linea in contenido:
        if linea.strip():  # Ignorar líneas vacías
            letra, valor = linea.split('\t')[0], int(linea.split('\t')[1])
            if letra not in max_min:
                # Inicializar máximo y mínimo con el primer valor encontrado
                max_min[letra] = {'max': valor, 'min': valor}
            else:
                # Actualizar máximo y mínimo según corresponda
                max_min[letra]['max'] = max(max_min[letra]['max'], valor)
                max_min[letra]['min'] = min(max_min[letra]['min'], valor)

    # Crear la lista de resultados ordenada alfabéticamente
    resultado = []
    for letra in sorted(max_min.keys()):
        resultado.append((letra, max_min[letra]['max'], max_min[letra]['min']))

    return resultado

print(pregunta_05())