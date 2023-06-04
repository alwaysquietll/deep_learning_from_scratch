import numpy as np

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    theta = np.sum(x*w) + b
    if theta <= 0:
        return 0
    else :
        return 1

if __name__ == '__main__':
    for x in [(0,0),(0,1),(1,0),(1,1)]:
        print("{} -> {}".format(str(x),OR(x[0], x[1])))