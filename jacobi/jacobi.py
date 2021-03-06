import numpy as np
from numpy import linalg as LA


# Método de Jacobi: x^(1) = C * x^(0) + g
def jacobi(A, x, b, guess, err_inf, n, pos, k_max=100, tol=1e-6):
    """This function returns the solution of the system of equations Ax = b by using the iterative Jacobi method """

    # print('A:')
    # print(A)

    diag = np.diag(A)
    # print('diag:')
    # print(diag)

    g = b/diag
    # print('g:')
    # print(g)

    C = -(A / diag[:, None])
    np.fill_diagonal(C,.0)
    # print('C:')
    # print(C)

    x_old = np.copy(guess)
    # print('x_old:')
    # print(x_old)

    error_norm = 1e6
    k = 0
    while k < k_max:

        x = C.dot(x_old) + g

        # residuum and residuum norm
        # res = b - np.dot(A, x)
        # res_norm = LA.norm(res, 2)

        # error and error norm
        err = -np.copy(x)
        err_norm = LA.norm(err, np.inf)

        # Calcule a norma do residuo e do erro absoluto
        # print("iter: %d  ||erro|| = %.9E  ||res|| = %.9E" % (k, err_norm, res_norm))

        # store error norm
        err_inf[k, pos] = err_norm

        # atualize o vetor antigo para o calculo da próxima aproximação
        x_old = np.copy(x)
        k = k + 1
    # end while

    # print('x:')
    # print(x)
    return x
