from plot_error import plot_err
from plot_log_error import plot_lerr
from plot_guess import plot_guess
from jacobi import jacobi
from gseidel import gseidel
from rb_gseidel import rb_gseidel
from wjacobi import wjacobi
import numpy as np
import matplotlib.pyplot as plt


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
def define_steady_state_problem(tpoints):
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

    # guess vector
    guess = np.zeros(npoints)

    # erro máximo
    err_inf = np.zeros((100, 9))

    # wave number (frequency)
    wavenumber = [1, 3, 6]

    # for error matrix storage
    pos = 0

    for k in range(3):
        aux = wavenumber[k] * np.pi / npoints
        for j in range(npoints):
            guess[j] = np.sin(aux * (j + 1))

        # x = jacobi(A, x, b, guess, err_inf, npoints, pos)
        x = wjacobi(A, x, b, guess, err_inf, w, npoints, pos)
        x = gseidel(A, x, b, guess, err_inf, npoints, pos+3)
        x = rb_gseidel(A, x, b, guess, err_inf, npoints, pos+6)
        pos = pos + 1
    # end for k


    # Print solution:

    # grid points coordinates
    # grid = np.zeros(npoints)
    # for k in range(npoints):
    #     grid[k] = k + 1
    # print(x)
    # fig, ax = plt.subplots()
    # ax.plot(grid, x, 'k')
    # ax.plot(grid, guess, 'r')
    # ax.set_xlabel('Grid points')
    # ax.set_ylabel('Solution:')
    # ax.grid(True)
    # # ax.set_yscale('log')
    # plt.show()

    # print('err_inf:')

    for k in range(9):
        maximum = err_inf[0, k]
        err_inf[:, k] = err_inf[:, k] / maximum

    plot_err(err_inf)
    plot_lerr(err_inf)
