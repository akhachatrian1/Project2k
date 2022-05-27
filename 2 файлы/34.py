from pickle import dump, load
from random import randint


#Cоздаем произвольное множество 
A = set()

for i in range(randint(3, 10)):
    A.add(randint(-15, 15))

f = open('Task34.pkl', 'wb')

dump(A, f) #Сохраненяем мн-во в файл

f.close()

f = open('Task34.pkl', 'rb')

S = load(f) #Считываем мн-во из файла

f.close()

print(S, type(S)) 


