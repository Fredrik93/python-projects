from elementsofai.cabin_prices_2 import fit_model


def test_predict():
    input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

    assert(fit_model(input_string) == "")