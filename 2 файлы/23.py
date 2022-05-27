from random import randint

def sort_(a): #Функция для сортировки списка в порядке возрастания 
    for i in range(len(a)-1):
        imin = i
        for j in range(i+1, len(a)):
            if a[j] < a[imin]:
                imin = j
        a[imin], a[i] = a[i], a[imin]

    return a

def create_2files(): #Функция, которая создает два файла с упорядоченными числами(в порядке возрастания)
    f1 = open('SortNumbers1.txt', 'w')
    f2 = open('SortNumbers2.txt', 'w')
    a = []
    b = []
    kolvo = randint(3,20)
    
    for i in range(kolvo):
        a.append(randint(-100,100))
        b.append(randint(-100,100))

    sort_(a)
    sort_(b)

    for i in range(kolvo):
        f1.write(str(a[i]) + ' ')
        f2.write(str(b[i]) + ' ')

    f1.close()
    f2.close()
                   

create_2files()

f1 = open('SortNumbers1.txt', 'r')
f2 = open('SortNumbers2.txt', 'r')
f3 = open('SortNumbers3.txt', 'w')
L = [] #Создаем список, в который запишем все числа из файлов


for line in f1:
    L += map(int, line.split())
for line in f2:
    L += map(int, line.split())

sort_(L) 

for i in range(len(L)):
    f3.write(str(L[i]) + ' ') #Записываем упорядоченные числа в новый файл

f1.close()
f2.close()
f3.close()

          
