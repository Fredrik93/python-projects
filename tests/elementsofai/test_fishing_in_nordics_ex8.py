from elementsofai.fishing_in_nordics_ex8 import main

def test_base_case():
    res = main()
    assert res == 0.2

def test_smoke():
    assert True