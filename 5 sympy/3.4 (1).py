from sympy import *
x = Symbol('x')
y = x**x

yprime = y.diff(x)
print("Производная x^x = ", yprime)
