# Este teste visa reproduzir o resultado do livro "A Multigrid Tutorial", Briggs.
# p15, figura 2.25

from wjacobi import wjacobi
from gseidel import gseidel
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from plot_guess import plot_guess


# Two point boundary value problem that describes the steady-state temperature distribution
# in a long uniform rod.
#
# -u"(x) + Su(x) = f(x),    0 < x < 1, S >= 0
#    u(0) = u(1) = 0.
#
# Simplifying, S = 0, and f(x) = 0, yields
#
# -u_(j-1) + 2u_j - u_(j+1) = 0,    1 <= j <= n-1
#                u_0 = u_n = 0.

# ssp_teste1: steady state problem teste1
def ssp_t1(tpoints):
    # npoints: number of free nodes
    # total de pontos: dirichlel + livres
    npoints = tpoints - 2

    # boundary conditions
    u_0 = 0
    u_n = 0

    # weighting factor
    w = 2/3

    # Matrix
    A = np.zeros((npoints, npoints))

    first = 0
    last = npoints - 1

    A[first, first] = 2
    A[first, first + 1] = -1
    A[last, last - 1] = -1
    A[last, last] = 2
    for i in range(first + 1, last):
        A[i, i - 1] = -1
        A[i, i] = 2
        A[i, i + 1] = -1

    # Right hand side vector
    b = np.zeros(npoints)
    b[first] = u_0
    b[last] = u_n

    # solution vector
    x = np.zeros(npoints)

    # erro máximo
    err_inf = np.zeros((100, 1))

    pos = np.arange(1, npoints+1, 1)
    v_indices = (np.pi/(npoints+1))*pos

    # guess vector
    guess = np.sin(v_indices)
    guess = guess + np.sin(6*v_indices)
    guess = guess + np.sin(32*v_indices)
    guess = (1/3)*guess

    wjacobi(A, x, b, guess, err_inf, w, npoints, 0)
    # gseidel(A, x, b, guess, err_inf, npoints, 0)

    maximum = err_inf[0, 0]
    err_inf[:, 0] = err_inf[:, 0] / maximum

    print(err_inf)

    fig, ax = plt.subplots()
    it = np.linspace(0, 100, 100)
    ax.plot(it, err_inf[:, 0], 'k--')

    ax.set_xlabel('Iterations')
    ax.set_ylabel('Error')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1)
    ax.grid(True)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(.25))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(.125))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(25))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(12.5))
    # ax.set_title('Weighted Jacobi method with ', r'$\omega = \frac{2}{3}$', ' and initial guess ', r'$(v_1 + v_2 + v_3)/3$')
    plt.show()

