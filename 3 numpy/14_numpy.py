from numpy import array, inf
from numpy.linalg import norm

n = int(input('Введите n - размер вектора >>> '))
print('Введите n чисел:')
list = [int(input()) for i in range(1, n + 1)]

vec = array(list)
print("Вектор: " )
print(vec)

norm_vec = norm(vec, inf)
print(norm_vec)
