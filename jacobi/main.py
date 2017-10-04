import numpy as np
from numpy import linalg as LA
# import math as mathfunc
# import matplotlib.pyplot as plt



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
            #end for j
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



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Main code starts here:
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

A = np.zeros((3, 3))
b = np.zeros(3)
x = np.zeros(3)

A[0,0] = -12
A[0,1] = 1
A[0,2] = 1.2
A[1,0] = 3.12
A[1,1] = -98.044
A[1,2] = 5.12
A[2,0] = 6.91
A[2,1] = 2.34
A[2,2] = -100.1

b[0] = -2
b[1] = 9.77
b[2] = -0.61

x = jacobi(A, x, b, 3)


print("\nSolution:")
print(x)
