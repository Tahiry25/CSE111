from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Tahiry', 'Ratsimanohatra') == "Ratsimanohatra; Tahiry"
    assert make_full_name('Allison', 'Jones') == "Jones; Allison"
    assert make_full_name('Yingtai-Han', 'Duàn') == "Duàn; Yingtai-Han"

def test_extract_family_name():
    assert extract_family_name('Ratsimanohatra; Tahiry') == "Ratsimanohatra"
    assert extract_family_name('Jones; Allison') == "Jones"
    assert extract_family_name('Duàn; Yingtai-Han') == "Duàn"

def test_extract_given_name():
    assert extract_given_name('Ratsimanohatra; Tahiry') == "Tahiry"
    assert extract_given_name('Jones; Allison') == "Allison"
    assert extract_given_name('Duàn; Yingtai-Han') == "Yingtai-Han"

pytest.main(["-v", "--tb=line", "-rN", __file__])