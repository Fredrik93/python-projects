from elementsofai.flip_the_coin_ex7 import main

def test_basic_case():
    res = main(2/3)
    res2 = main(1)
    assert res is not None