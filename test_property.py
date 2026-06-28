from hypothesis import given, strategies as st
from binario import busqueda_binaria

@given(st.lists(st.integers(), unique=True).map(sorted))
def test_si_encuentra_el_indice_correcto(lista):

    if len(lista) == 0:
        return
    objetivo = lista[len(lista)//2]
    indice = busqueda_binaria(lista, objetivo)
    assert lista[indice] == objetivo
    
@given(st.lists(st.integers(), unique=True).map(sorted))
def test_si_no_existe_devuelve_menos_uno(lista):
    objetivo = 999999999
    if objetivo in lista:
        return
    assert busqueda_binaria(lista, objetivo) == -1
    