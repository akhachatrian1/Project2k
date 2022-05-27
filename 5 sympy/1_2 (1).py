from sympy import *
x = Symbol('x')
expr = Limit((3*x*x + 2*x + 1)/(2*x*x*x - x), x, 0)
print(expr," = ", expr.doit())
expr1 = Limit((3*x*x + 2*x + 1)/(2*x*x*x - x), x, 0, '+')
print("Правосторонний предел: ", expr1," = ", expr1.doit())
expr2 = Limit((3*x*x + 2*x + 1)/(2*x*x*x - x), x, 0, '-')
print("Левосторонний предел: ", expr2," = ", expr2.doit())
