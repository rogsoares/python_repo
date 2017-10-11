import numpy as np
from numpy import linalg as LA


# Weighted Jacobi Method
def wjacobi(A, x, b, guess, err_inf, w, n, pos, k_max=100, k=None):
    """This function returns the solution of the system of equations Ax = b by using the iterative Jacobi method
    """

    x_old = guess
    # err_norm = 1e6
    identity = np.eye(n)
    print('identity: ')
    print(identity)

    d = np.diag(A)
    print('d: ')
    print(d)

    diagonal = np.zeros(n)
    for i in range(n):
        diagonal[i] = 1./d[i]

    print('diagonal: ')
    print(diagonal)

    diag_inv = np.zeros((n, n))
    np.fill_diagonal(diag_inv, diagonal)
    print('diag_inv: ')
    print(diag_inv)

    # L = np.tril(A, k=-1)
    # U = np.triu(A, k=1)
    # Rj = diag_inv * (L + U)

    Rj = A
    print('Rj: ')
    np.fill_diagonal(Rj, .0)
    print(Rj)
    Rj = diag_inv.dot(Rj)
    print(Rj)

    Rw = (1 - w) * identity + w * Rj
    print('Rw: ')
    print(Rw)

    k = 0
    while k < k_max:
        x = Rw.dot(x_old) + w*diag_inv.dot(b)

        # res = b - np.dot(A, x)
        err = -x

        # Calcule a norma do residuo e do erro absoluto
        err_inf[k, pos] = LA.norm(err, np.inf)

        # atualize o vetor antigo para o calculo da próxima aproximação
        x_old = np.copy(x)

        k = k + 1
    # end while

    return x