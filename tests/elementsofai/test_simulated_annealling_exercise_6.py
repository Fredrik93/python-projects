import numpy as np
import pytest
import sys
from elementsofai.simulated_annealling_exercise_6 import generator
def test_generator_at_origin():
    """Test generator function at origin"""
    result = generator(0, 0, x0=0.0, y0=0.0)
    assert isinstance(result, (int, float, np.number))

def test_generator_with_offset():
    """Test generator function with different offsets"""
    result1 = generator(50, 50, x0=0.0, y0=0.0)
    result2 = generator(50, 50, x0=0.5, y0=0.5)
    assert result1 != result2

def test_generator_range():
    """Test that generator values are in expected range"""
    result = generator(25, 25, x0=0.0, y0=0.0)
    assert -3 <= result <= 3  # Based on sin and cos functions

def test_generator_symmetry():
    """Test generator symmetry properties"""
    result1 = generator(25, 25, x0=0.0, y0=0.0)
    result2 = generator(25, 25, x0=0.0, y0=0.0)
    assert result1 == result2  # Same inputs should give same output

def test_generator_different_points():
    """Test that different points can give different values"""
    result1 = generator(10, 10, x0=0.0, y0=0.0)
    result2 = generator(80, 80, x0=0.0, y0=0.0)
    assert result1 != result2

