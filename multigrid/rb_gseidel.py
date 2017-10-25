import numpy as np
from numpy import linalg as LA


# Método de Jacobi: x^(1) = C * x^(0) + g
def rb_gseidel(A, x, b, guess, err_inf, n, pos, k_max=100, tol=1e-6):
    """This function returns the solution of the system of equations Ax = b by using the iterative Jacobi method """

    x_old = np.copy(guess)
    x[0:n] = 0

    k = 0
    while k < k_max:

        x[0] = 0.5 * (x_old[1] + b[0])
        for i in range(2,n,2):
            x[i] = 0.5*(x_old[i-1] + x_old[i+1])

        for i in range(1,n-1,2):
            x[i] = 0.5*(x[i-1]+x[i+1])
        x[n-1] = 0.5 * (x[n - 2] + b[n-1])

        # residuum and residuum norm
        res = b - np.dot(A, x)
        res_norm = LA.norm(res, 2)

        # error and error norm
        err = -np.copy(x)
        err_norm = LA.norm(err, np.inf)

        # Calcule a norma do residuo e do erro absoluto
        print("iter: %d  ||erro|| = %.9E  ||res|| = %.9E" % (k, err_norm, res_norm))

        # store error norm
        err_inf[k, pos] = err_norm

        # atualize o vetor antigo para o calculo da próxima aproximação
        x_old = np.copy(x)
        k = k + 1
    # end while

    # print('x:')
    # print(x)
    return x
