from numpy import array

n_1 = int(input('Введите n_1 - размер вектора >>> '))
print('Введите n_1 чисел (горизонтальный вектор):')
list_1 = [int(input()) for i in range(1, n_1 + 1)]

vec_1 = array(list_1)
print("Горизонтальный вектор: " )
print(vec_1)


n_2 = int(input('Введите n_2 - размер вектора >>> '))
print('Введите n_2 чисел (вертикальный вектор):')
list_2 = [[int(input())] for i in range(1, n_2 + 1)]

vec_2 = array(list_2)
print("Вертикальный вектор: " )
print(vec_2)
