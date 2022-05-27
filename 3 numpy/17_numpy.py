import numpy as np
from random import *

n = randint(1, 4)
a = [[randint(-10,10) for i in range(n)] for i in range(n)] #Создаем случайную кв. матрицу

A = np.array(a)
Det_ = round(np.linalg.det(A,)) #Вычисляем определитель

print('Квадратная матрица А:', A , sep = '\n')
print()
print('Определитель матрицы А = ', Det_)
