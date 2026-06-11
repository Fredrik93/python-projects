
import numpy as np 

interpol = np.interp(2.5, [0.0, 1.0, 2.0, 3.0, 4.0], [-0.7568025,-0.9290145,-0.81332930,.6569866,0.09131724])

# asnser: -0.07817134999999997
print(interpol)
