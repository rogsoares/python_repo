
import math as mathfunc
# It provides access to the mathematical functions defined by the C standard.

import numpy as np
# NumPy is the fundamental package for scientific computing with Python.
# It contains among other things:
#     a powerful N-dimensional array object
#     sophisticated (broadcasting) functions
#     tools for integrating C/C++ and Fortran code
#     useful linear algebra, Fourier transform, and random number capabilities.
# Besides its obvious scientific uses, NumPy can also be used as an efficient
# multi-dimensional container of generic data. Arbitrary data-types can be
# defined. This allows NumPy to seamlessly and speedily integrate with a
# wide variety of databases.

import matplotlib.pyplot as plt
# Matplotlib is a Python 2D plotting library which produces
# publication quality figures in a variety of hardcopy formats
# and interactive environments across platforms.


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Approximating a Derivative by a Difference Quotient and Centered Differences
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

h = np.empty(20)
error = np.empty((20,2))

n = 0
h_old = 1.0;
x = 1.0

deriv = mathfunc.cos(x)
print('\n\nderiv = %.7e' %(deriv))

while (n < 20):
    h_new = h_old/10
    h_old = h_new
    diffquo = (mathfunc.sin(x + h_new) - mathfunc.sin(x)) / h_new
    cdiffquo = (mathfunc.sin(x + h_new) - mathfunc.sin(x - h_new))/(2*h_new)

    h[n] = h_new
    error[n,0] = abs(deriv - diffquo)
    error[n,1] = abs(deriv - cdiffquo)
    n += 1

print('      h            error')
for i in range(20):
    print('%.16f  %.16f  %.16f'% (h[i],error[i,0],error[i,1]))


print(np.finfo(float).eps)


x = np.linspace(0, 10, 500)
dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off

fig, ax = plt.subplots()
line1, = ax.plot(h, error[:,0], 'k^', linewidth=2, label='Diferença dividida')
ax.set_xscale('log')
ax.set_yscale('log')


line2, = ax.plot(h,error[:,1], 'bo', label='Diferença centrada')
ax.set_xscale('log')
ax.set_yscale('log')

ax.legend(loc='lower left')
ax.set_xlabel('h')
ax.set_ylabel('Erro')
ax.set_title('Comparação entre dois esquemas de\naproximação de derivada')
ax.set_xlim(10^(-20),10^(0))
ax.grid(True)
plt.show()
