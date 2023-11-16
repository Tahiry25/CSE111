from address import extract_city, extract_state, extract_zipcode
import pytest

full_address = '525 S Center St, Rexburg, ID 83460'

def test_extract_city():
    assert extract_city(full_address) == "Rexburg"

def test_extract_state():
    assert extract_state(full_address) == "ID"

def test_extract_zipcode():
    assert extract_zipcode(full_address) == "83460"

pytest.main(["-v", "--tb=line", "-rN", __file__])