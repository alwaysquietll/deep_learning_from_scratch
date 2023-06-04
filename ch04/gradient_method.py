import matplotlib.pyplot as plt
import numpy as np
from gradient_2d import numerical_gradient,function_2

def gradient_descent(f, init_x, lr=0.01, step_number=100):
    x = init_x
    x_history = []

    for i in range(step_number):
        x_history.append(x.copy())

        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, np.array(x_history)


if __name__ == '__main__':
    init_x = np.array([-3.0,4.0])
    # print(gradient_descent(function_2, init_x, lr=0.1, step_number=100))
    lr = 0.1
    step_number = 20
    x, x_history = gradient_descent(function_2, init_x, lr, step_number)

    plt.plot( [-5, 5], [0, 0], '--b')
    plt.plot( [0, 0], [-5, 5], '--b')
    plt.plot(x_history[:,0], x_history[:,1], 'o')

    plt.xlim(-3.5, 3.5)
    plt.ylim(-4.5, 4.5)
    plt.xlabel('X0')
    plt.ylabel('X1')
    plt.show()