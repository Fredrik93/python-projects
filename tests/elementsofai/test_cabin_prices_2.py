from elementsofai.cabin_prices_2 import find_best


def test_predict():
    assert(find_best(1,1,1) == 1)