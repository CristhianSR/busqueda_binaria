from binario import busqueda_binaria

def test_elemento_encontrado():
    lista = [1, 3, 5, 7, 9]
    assert busqueda_binaria(lista, 5) == 2

def test_elemento_no_encontrado():
    lista = [1, 3, 5, 7, 9]
    assert busqueda_binaria(lista, 4) == -1

def test_primer_elemento():
    lista = [2, 4, 6, 8]
    assert busqueda_binaria(lista, 2) == 0

def test_ultimo_elemento():
    lista = [2, 4, 6, 8]
    assert busqueda_binaria(lista, 8) == 3

def test_lista_vacia():
    lista = []
    assert busqueda_binaria(lista, 10) == -1