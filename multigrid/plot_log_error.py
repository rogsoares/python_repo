import matplotlib.pyplot as plt
import numpy as np


def plot_lerr(err_inf):
    fig, ax = plt.subplots()
    x = np.linspace(0, 100, 100)
    ax.plot(x, err_inf[:, 0], 'k--', linewidth=1)
    # ax.annotate('k = 1', (x[90], err_inf[82, 0]))
    ax.plot(x, err_inf[:, 1], 'r--', linewidth=1)
    # ax.annotate('k = 3', (x[90], err_inf[85, 1]))
    ax.plot(x, err_inf[:, 2], 'b--', linewidth=1)
    # ax.annotate('k = 6', (x[90], err_inf[85, 2]))

    ax.plot(x, err_inf[:, 3], 'k.', markevery=5, linewidth=1)
    # ax.annotate('k = 1', (x[90], err_inf[82, 0]))
    ax.plot(x, err_inf[:, 4], 'r.', markevery=5, linewidth=1)
    # ax.annotate('k = 3', (x[90], err_inf[85, 1]))
    ax.plot(x, err_inf[:, 5], 'b.', markevery=5, linewidth=1)

    ax.plot(x, err_inf[:, 6], 'k^', markevery=5, linewidth=1)
    # ax.annotate('k = 1', (x[90], err_inf[82, 0]))
    ax.plot(x, err_inf[:, 7], 'r^', markevery=5, linewidth=1)
    # ax.annotate('k = 3', (x[90], err_inf[85, 1]))
    ax.plot(x, err_inf[:, 8], 'b^', markevery=5, linewidth=1)
    # ax.legend(loc='upper right')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Error')
    ax.set_xlim(0, 100)
    ax.set_yscale('log')
    ax.grid(True)
    ax.set_title('Compotamento do erro para três métodos iterativos.')
    plt.show()
