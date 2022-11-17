import numpy as np
import matplotlib.pyplot as plt


def f(x, noise_level=0.1):
    return np.sin(5 * x[0]) * (1 - np.tanh(x[0] ** 2))\
           + np.random.randn() * noise_level

def print_fun(func, noise_level):
    # Plot f(x) + contours

    x = np.linspace(-2, 2, 400).reshape(-1, 1)
    fx = [func(x_i, noise_level=0.0) for x_i in x]
    plt.plot(x, fx, "r--", label="True (unknown)")
    plt.fill(np.concatenate([x, x[::-1]]),\
    np.concatenate(([fx_i - 1.9600 * noise_level for fx_i in fx],\
    [fx_i + 1.9600 * noise_level for fx_i in fx[::-1]])),\
    alpha=.2, fc="r", ec="None")
    plt.legend()
    plt.grid()
    plt.show()
