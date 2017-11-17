import matplotlib.pyplot as plt
import numpy as np


def plot_err(err_inf):

    fig, ax = plt.subplots()
    x = np.linspace(0, 100, 100)
    ax.plot(x, err_inf[:, 0], 'k--', linewidth=1)
    # ax.annotate('k = 1', (x[90], err_inf[82, 0]))
    ax.plot(x, err_inf[:, 1], 'r--', linewidth=1)
    # ax.annotate('k = 3', (x[90], err_inf[85, 1]))
    ax.plot(x, err_inf[:, 2], 'b--', linewidth=1)
    # ax.annotate('k = 6', (x[90], err_inf[85, 2]))

    ax.plot(x, err_inf[:, 3], 'k', linewidth=1)
    # ax.annotate('k = 1', (x[90], err_inf[82, 0]))
    ax.plot(x, err_inf[:, 4], 'r', linewidth=1)
    # ax.annotate('k = 3', (x[90], err_inf[85, 1]))
    ax.plot(x, err_inf[:, 5], 'b', linewidth=1)
    # ax.annotate('k = 6', (x[90], err_inf[85, 2]))

    ax.plot(x, err_inf[:, 6], 'k^', linewidth=1)
    # ax.annotate('k = 1', (x[90], err_inf[82, 0]))
    ax.plot(x, err_inf[:, 7], 'r^', linewidth=1)
    # ax.annotate('k = 3', (x[90], err_inf[85, 1]))
    ax.plot(x, err_inf[:, 8], 'b^', linewidth=1)
    # ax.annotate('k = 6', (x[90], err_inf[85, 2]))

    ax.set_xlabel('Iterations')
    ax.set_ylabel('Error')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1)
    #
    ax.set_title('Comportamento do erro para três métodos iterativos.')
    ax.grid(True)
    plt.show()
    