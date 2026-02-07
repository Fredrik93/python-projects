from elementsofai.nearest_neighbour import nearest
import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def test():
    result = nearest(x_train, x_test)
    assert result >= 0 and result < len(x_train)
    print("Test passed!")

