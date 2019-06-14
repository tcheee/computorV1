import numpy as np
import matplotlib.pyplot as plt

def draw(a, b, c):
    x = np.linspace(-20, 20, 256, endpoint = True)
    y = (a * (x * x)) + (b * x) + c
    plt.plot(x, y, '-r', label="y = " + str(a) + "X^2 + " + str(b) + "X + " + str(c))
    axes = plt.gca()
    axes.set_xlim([x.min(), x.max()])
    axes.set_ylim([y.min(), y.max()])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Curve')
    plt.legend(loc='upper left')
    plt.show()