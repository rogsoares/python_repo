from plot_error import plot_err
from plot_guess import plot_guess
from jacobi import jacobi
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
def define_steady_state_problem(npoints):

    # npoints: number of free nodes

    # boundary conditions
    u_0 = 1
    u_n = 0

    # weighting factor
    w = 1

    # Matrix
    A = np.zeros((npoints, npoints))

    first = 0
    last = npoints - 1

    A[first, first] = 2
    A[first, first+1] = -1
    A[last, last-1] = -1
    A[last, last] = 2
    for i in range(first+1, last):
        A[i, i - 1] = -1
        A[i, i] = 2
        A[i, i + 1] = -1

    # Right hand side vector
    b = np.zeros(npoints)
    b[0] = u_0
    b[npoints - 1] = u_n

    # solution vector
    x = np.zeros(npoints)

    # guess vector
    guess = np.zeros(npoints)

    # erro máximo
    err_inf = np.zeros((100, 9))

    # grid points coordinates
    h = 1/(npoints+1)
    grid = np.zeros(npoints)
    for k in range(npoints):
        grid[k] = (k+1)*h

    # wave number (frequency)
    pos = 0
    wnum = [1, 3, 6]
    for k in range(1):
        # c = wnum[k]*np.pi/(npoints+2)
        # for j in range(0, npoints):
        #     guess[j] = .0 #np.sin((j+1)*c)
        # end for j

        # x = jacobi(A, x, b, guess, err_inf, npoints, pos)
        x = wjacobi(A, x, b, guess, err_inf, w, npoints, pos)

        pos = pos + 1
    # end for k

    # Print solution:
    print(x)
    fig, ax = plt.subplots()
    ax.plot(grid, x, 'k')
    plt.show()

    # print(err_inf)
    # for k in range(1):
    #     maximum = err_inf[0, k]
    #     err_inf[:, k] = err_inf[:, k]/maximum
    #
    # plot_err(err_inf)