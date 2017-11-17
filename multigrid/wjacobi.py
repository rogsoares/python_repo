import numpy as np
from numpy import linalg as LA


# Weighted Jacobi Method
def wjacobi(A, x, b, guess, err_inf, w, n, pos, k_max=100, k=None):
    """This function returns the solution of the system of equations Ax = b by using the iterative Jacobi method
    """

    x_old = np.copy(guess)

    identity = np.eye(n)
    d = np.diag(A)

    diagonal = np.zeros(n)
    for i in range(n):
        diagonal[i] = 1./d[i]

    diag_inv = np.zeros((n, n))
    np.fill_diagonal(diag_inv, diagonal)


    Rj = np.copy(A)
    np.fill_diagonal(Rj, .0)
    Rj = diag_inv.dot(Rj)
    Rw = (w - 1) * identity + w * Rj
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