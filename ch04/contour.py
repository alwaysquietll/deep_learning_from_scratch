import numpy as np
import matplotlib.pyplot as plt
from gradient_2d import numerical_gradient,function_2

def gradient_descent(f, init_x, lr=0.01, step_number=100):
    x = init_x
    x_history = []

    for i in range(step_number):
        x_history.append(x.copy())

        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, np.array(x_history)
# 定义二元函数
def f(x, y):
    return np.sin(x) + np.cos(y)

# 定义绘制等高线图的函数
def plot_contour(f):
    x = np.linspace(-3.5, 3.5)
    y = np.linspace(-4.5, 4.5)
    X, Y = np.meshgrid(x, y)
    Z = f(np.array([X, Y]))

    plt.figure()
    plt.contour(X, Y, Z)
    plt.xlabel('x')
    plt.ylabel('y')


if __name__ == '__main__':
    # 绘制等高线图
    plot_contour(function_2)

    # 运行梯度下降算法并绘制轨迹
    init_x = np.array([-3.0, 4.0])
    lr = 0.1
    step_number = 20
    x, x_history = gradient_descent(function_2, init_x, lr, step_number)
    plt.plot(x_history[:, 0], x_history[:, 1], 'o', color='red')

    # 显示图像
    plt.show()