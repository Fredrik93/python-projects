import numpy as np
import pytest
import sys
from elementsofai.simulated_annealling_exercise_6 import mountains, main

def test_main_returns_valid_position():
    h = mountains(100)
    result = main(h, 50)
    assert 0 <= result < len(h)
