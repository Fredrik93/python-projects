# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
import numpy as np

X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
C = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, C):
    for mokki in X:
        price = np.array(mokki) @ np.array(C)
        print(price)


predict(X, C)
