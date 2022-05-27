from random import randint 

f = open('task3.txt', 'w')

n1 = int(input('Введите n1 >>> '))
n2 = int(input('Введите n2 >>> '))
m = abs(int(input('Введите m >>> ')))

kolvo = randint(n1,n2)

for i in range(kolvo):
    a = str(randint(-m,m))
    f.write(a + ' ')

f.close()    
