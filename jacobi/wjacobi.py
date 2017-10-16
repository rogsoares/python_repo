import numpy as np
from numpy import linalg as LA


# Weighted Jacobi Method
def wjacobi(A, x, b, guess, err_inf, w, n, pos, k_max=100, k=None):
    """This function returns the solution of the system of equations Ax = b by using the iterative Jacobi method
    """

    x_old = np.copy(guess)
    # print(b)
    # err_norm = 1e6
    identity = np.eye(n)
    # print('identity: ')
    # print(identity)

    # OK

    d = np.diag(A)
    # print('d: ')
    # print(d)

    # OK

    diagonal = np.zeros(n)
    for i in range(n):
        diagonal[i] = 1./d[i]

    # print('diagonal: ')
    # print(diagonal)

    # OK

    diag_inv = np.zeros((n, n))
    np.fill_diagonal(diag_inv, diagonal)
    # print('diag_inv: ')
    # print(diag_inv)

    # OK
    # L = np.tril(A, k=-1)
    # U = np.triu(A, k=1)
    # Rj = diag_inv * (L + U)

    Rj = np.copy(A)
    # print('Rj: ')
    np.fill_diagonal(Rj, .0)
    # print(Rj)
    Rj = diag_inv.dot(Rj)
    # print(Rj)

    # OK
    Rw = (w - 1) * identity + w * Rj
    # print('Rw_part_1: ')
    # print(Rw_part_1)
    # print('RRw_part_2: ')
    # print(Rw_part_2)
    # print('Rw: ')
    # print(Rw)

    aux = w * diag_inv.dot(b)

    k = 0
    while k < k_max:
        x = Rw.dot(x_old) + aux

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

    return x