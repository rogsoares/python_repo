import numpy as np
import random
import matplotlib.pyplot as plt


def eingenvalues(n):
    # weighting values
    w = np.array([1 / 3, 1 / 2, 2 / 3, 1])

    # step
    step = n / 200

    # Continuous modes: k
    k = np.arange(0, n, step)

    # plot
    fig, ax = plt.subplots()

    # autovalores de Rw
    for i in range(len(w)):
        ev_Rw = 1 - 2 * w[i] * (np.sin(np.pi * k / (2 * n)) ** 2)
        ax.plot(k, ev_Rw, label='bosta')

    ax.set_xlabel('k')
    ax.set_ylabel(r'$\lambda_{k}(R_{\omega})$')
    ax.set_xlim(0, n)
    ax.set_title('Eingenvalues of the interation matrix ' + r'$R_{\omega}$')
    ax.grid(True)
    plt.show()
