import pytest
from icontract.errors import ViolationError
from binario import busqueda_binaria

def test_contrato_lista_ordenada():
    with pytest.raises(ViolationError):
        busqueda_binaria([5,2,8], 2)

def test_contrato_resultado():
    assert busqueda_binaria([1,2,3,4,5],4) == 3