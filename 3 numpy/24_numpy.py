import numpy as np

x = np.random.randint(-20, 20, 5)

sr_z = np.nanmean(x)
disp = np.nanvar(x)
med  = np.nanmedian(x)

print('Массив X = ', x)
print('Среднее значение элементов X =', sr_z)
print('Дисперсия элементов X =','%.3f' % disp)
print('Медиана элементов X =', med)
