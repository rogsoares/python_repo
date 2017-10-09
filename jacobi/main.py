import numpy as np
from numpy import linalg as LA

import matplotlib.pyplot as plt
# Matplotlib is a Python 2D plotting library which produces
# publication quality figures in a variety of hardcopy formats
# and interactive environments across platforms.



# import math as mathfunc
# import matplotlib.pyplot as plt


# Método de Jacobi
def jacobi(A, x, b, n, k_max=100, tol=1e-6):
    """This function returns the solution of the system of equations Ax = b by using the iterative Jacobi method """

    x_old = np.zeros(n)
    error_norm = 1e6
    k = 0
    while error_norm > tol and k < k_max:
        # Para cada incógnita 'i'
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s = s + A[i, j] * x_old[i]
                    # end if
            # end for j
            x[i] = (b[i] - s) / A[i, i]
        # end for i

        res = b - np.dot(A, x)
        error = x - x_old

        # Calcule a norma do residuo e do erro absoluto
        res_norm = LA.norm(res, 2)
        error_norm = LA.norm(error, 2)
        print("iter: %d  ||erro|| = %.9E  ||res|| = %.9E" % (k, error_norm, res_norm))

        # atualize o vetor antigo para o calculo da próxima aproximação
        x_old = np.copy(x)
        k = k + 1
    # end while

    if k == k_max:
        print("\n\nMaximum number of iterations reached! %d" % k_max)
    else:
        print("\n\nNumber of iterations reached: %d" % k)

    return x


# Apenas uma caso para testar o metodo de JAcobi
def case1(event=None):
    A = np.zeros((3, 3))
    b = np.zeros(3)
    x = np.zeros(3)

    A[0, 0] = -12
    A[0, 1] = 1
    A[0, 2] = 1.2
    A[1, 0] = 3.12
    A[1, 1] = -98.044
    A[1, 2] = 5.12
    A[2, 0] = 6.91
    A[2, 1] = 2.34
    A[2, 2] = -100.1

    b[0] = -2
    b[1] = 9.77
    b[2] = -0.61

    x = jacobi(A, x, b, 3)

    print("\nSolution:")
    print(x)


# Weighted Jacobi Method
def wjacobi(A, x, b, guess, err_inf, w, n, pos, k_max=100, k=None):
    """This function returns the solution of the system of equations Ax = b by using the iterative Jacobi method
    """

    x_old = guess
    # err_norm = 1e6
    identity = np.eye(n)
    diag_inv = np.zeros((n, n))
    for i in range(n):
        diag_inv[i, i] = 1 / A[i, i]

    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)
    Rj = diag_inv * (L + U)
    Rw = (1 - w) * identity + w * Rj

    k = 1
    while k <= k_max:
        x = Rw * x_old

        # res = b - np.dot(A, x)
        err = -x

        # Calcule a norma do residuo e do erro absoluto
        err_inf[k-1, pos] = LA.norm(err, np.inf)

        # atualize o vetor antigo para o calculo da próxima aproximação
        x_old = np.copy(x)
        k = k + 1
    # end while

    return x


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
    u_0 = 0
    u_n = 0

    # weighting factor
    w = 2 / 3

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

    # wave number (frequency)
    i = 0
    wavenumbers = [1, 3, 6]
    for k in range(3):
        c = wavenumbers[k]*np.pi/npoints
        for j in range(0,npoints):
            guess[j] = np.sin((j+1)*c)
        # end for j

        wjacobi(A, x, b, guess, err_inf, w, npoints, i)
        i = i + 1
    # end for k

    ploterr(err_inf)


def ploterr(err_inf):
    fig, ax = plt.subplots()

    xx = np.linspace(1, 100, 100)
    print('xx')
    print(xx)

    print('\nerr_inf[:,0]')
    print(err_inf[:,0])

    ax.plot(xx, err_inf[:, 2], 'k', linewidth=1, label='Diferença dividida')
    ax.set_yscale('log')
    ax.legend(loc='upper right')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Error')
    ax.set_title('Comparação entre dois esquemas de\naproximação de derivada')
    ax.grid(True)
    plt.show()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Main code starts here:
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

define_steady_state_problem(64)
