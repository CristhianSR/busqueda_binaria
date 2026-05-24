def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        mitad = (inicio + fin) // 2

        if lista[mitad] == objetivo:
            return mitad

        elif lista[mitad] < objetivo:
            inicio = mitad + 1

        else:
            fin = mitad - 1

    return -1
