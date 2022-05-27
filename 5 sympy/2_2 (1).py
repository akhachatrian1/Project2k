from sympy import *
n = Symbol('n')
expr = Sum(1/n/n,(n, 1, oo))
print(expr," = ", expr.doit())

