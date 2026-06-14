from binario import busqueda_binaria

def test_elemento_encontrado():
    lista = [1, 3, 5, 7, 9]
    assert busqueda_binaria(lista, 5) == 2

test_elemento_encontrado()