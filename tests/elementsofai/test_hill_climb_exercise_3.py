from elementsofai.hill_climb_exercise_3 import climb, h

def test_climb_returns_int():
        result = climb(50, h)
        assert isinstance(result, int), "climb() should return an integer"

def test_climb_within_bounds():
        result = climb(50, h)
        assert result == -1 or (0 <= result < len(h)), "climb() should return a valid index or -1"

def test_climb_from_different_positions():
        result1 = climb(25, h)
        result2 = climb(75, h)
        assert isinstance(result1, int) and isinstance(result2, int), "climb() should work from different starting positions"