import numpy as np
from numpy import linalg as LA


# Método de Jacobi: x^(1) = C * x^(0) + g
def gseidel(A, x, b, guess, err_inf, n, pos, k_max=100, tol=1e-6):
    """This function returns the solution of the system of equations Ax = b by using the iterative Jacobi method """

    # extract matrix diagonal
    diag = np.diag(A)

    # create g vector
    g = b/diag

    # define a matrix
    full_mat = -(A / diag[:, None])
    np.fill_diagonal(full_mat, .0)

    # define upper and low traingular matrices
    upper_mat = np.triu(full_mat, k=1)
    low_mat = np.tril(full_mat, k=0)

    # print('full_mat')
    # print(full_mat)
    # print('upper_mat')
    # print(upper_mat)
    # print('low_mat')
    # print(low_mat)

    x_old = np.copy(guess)
    x[0:n] = 0

    k = 0
    while k < k_max:

        x = g + upper_mat.dot(x_old) + low_mat.dot(x)
        # x = x + low_mat.dot(x)

        # residuum and residuum norm
        res = b - np.dot(A, x)
        res_norm = LA.norm(res, 2)

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
