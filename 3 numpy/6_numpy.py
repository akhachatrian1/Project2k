import numpy

list_1 = [1, 2, 3, 4]
list_2 = [[1], [2], [3]]
list_3 = ['1', '2', '3', '4', '5']
list_4 = [[1.1, 2.2], [3.3, 4.4]]
list_5 = [[-1, -2], [3.3, 4.4]]

vec_list = [list_1, list_2, list_3, list_4, list_5]
for list in vec_list:
    vec = numpy.array(list)
    print("Вектор >> ")
    print(vec)

    print("Тип элементов массива (dtype) >> ", vec.dtype)
    print("Число измерений массива (ndim) >> ", numpy.ndim(vec))
    print("Размерность массива (shape) >> ", numpy.shape(vec))
    print("Количество элементов в массиве (size) >> ", numpy.size(vec))
    print("Размер каждого элемента массивв в байтах (itemsize) >> ", vec.itemsize)
    print("Количество пространства в байтах (nbytes) >> ", vec.nbytes, '\n')
