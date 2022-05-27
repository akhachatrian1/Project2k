from sympy import *
x = Symbol('x')
ans = solve(Eq(x*x*x-x*x-22*x+40, 0), x)
print("Все вещественные и комплексные корни полинома: ", ans)
