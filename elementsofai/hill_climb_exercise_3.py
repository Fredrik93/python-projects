import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 

w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    leftSteps = 5;
    rightSteps = 5;

    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        print("entered")
        summit = True         # stop unless there's a way up
        if h[x + 1] > h[x]:
            x = x + 1
            rihtSteps = rightSteps-1         # right is higher, go there
            summit = False
            print("rightSteps count: ", rightSteps)    # and keep going
        elif h[x-1] > h[x]:
            x = x - 1
            summit = False
            leftSteps = leftSteps-1
            print("leftsteps count: ", leftSteps)
    
    if leftSteps == 0: 
        print("entered leftSteps 0: ", x)
        return x
    if rightSteps == 0:
        print("entered rightSteps 0: ", x)
        return x
    return -1


def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

main(h)
