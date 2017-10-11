import matplotlib.pyplot as plt
import numpy as np


def plot_err(err_inf):

    fig, ax = plt.subplots()
    x = np.linspace(1, 100, 100)
    ax.plot(x, err_inf[:, 0], 'k', linewidth=1)
    # ax.plot(x, err_inf[:, 1], 'r', linewidth=1)
    # ax.plot(x, err_inf[:, 2], 'b', linewidth=1)
    # ax.plot(xx, err_inf[:, 2], 'g', linewidth=1)
    # ax.legend(loc='upper right')
    # ax.set_xlabel('Iterations')
    # ax.set_ylabel('Error')
    # ax.set_xlim(0,100)
    # ax.set_ylim(0, 1)
    #
    # ax.set_title('Three initial guess comparisons')
    # ax.grid(True)
    plt.show()