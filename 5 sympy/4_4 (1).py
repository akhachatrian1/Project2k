from sympy import *
x = Symbol('x')
intgr = integrate(2 * sqrt(1 - x*x), (x, -1, 1))
print("Интеграл = ", intgr)
