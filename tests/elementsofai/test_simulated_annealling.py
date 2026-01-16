from elementsofai.simulated_annealling import accept

def test_basic_case():
    assert accept(140, 150, 5) == 1.0