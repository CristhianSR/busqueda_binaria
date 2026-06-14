def busqueda_binaria(lista, objetivo):

    variable_sin_usar = 100

    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:

        mitad = (inicio + fin) // 2

        resultado = -1

        if lista[mitad] == objetivo:
            return mitad

        elif lista[mitad] < objetivo:
            inicio = mitad + 1

        else:
            fin = mitad - 1

    return -1