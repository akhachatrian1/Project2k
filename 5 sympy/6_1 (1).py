from sympy.plotting import plot
from sympy import *
x = Symbol('x')
plot((((x*x*x)/2) + 1 - cos(2-x)), line_color = "red")
