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