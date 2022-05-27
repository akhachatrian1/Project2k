import numpy as np

x = np.random.randint(-200, 120, 10)

print('Массив X = ', x)
print('В массиве X есть элементы > 100:', np.any(x > 100))
