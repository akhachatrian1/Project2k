from tkinter import * # подключение tkinter
from math import * # подключение математического модуля

# создание окна
root  =  Tk( )
root.title("Обработка списка K")

# создание фрейма для формул
win1 = Frame(root)
win1.pack(anchor = 'n')

# метка я надписью Формулы:
Label(win1, text='Формулы:').pack(side=LEFT, padx=10, pady=10, expand=YES, fill=X)

# создание формул
F1 = Entry(win1)
F1.pack(side=LEFT, padx=10, pady=10, expand=YES, fill=X)
F2 = Entry(win1)
F2.pack(side=LEFT, padx=10, pady=10, expand=YES, fill=X)
F1.insert(0, "x + 1")
F2.insert(0, "x * 2")


# создание фрейма для кнопки
win2 = Frame(root)
win2.pack()

# описание функции для кнопки
def change_of_labels():
     cycle()
     for i in range(11):
          List_of_labels[i]['text'] = K[i]
# создание кнопки
Button(win2, text = 'Запуск обработки списка  K', command=change_of_labels).pack()

# создание фрейма для вывода исходного списка K
win3 = Frame(root)
win3.pack()

# создание списка K
K = [0,1,0,0,0,0,0,0,0,0,0]
# вывод исходного списка K
for i in range(11):
     Label(win3, text=str(K[i])).pack(side=LEFT, padx=10, pady=10, expand=YES, fill=X)

# создание фрейма для вывода измененного списка K
win4 = Frame(root)
win4.pack()

# создание меток для вывода измененного списка K
List_of_labels = []
for i in range(11):
     List_of_labels.append(Label(win4, text=str(K[i])))
     List_of_labels[i].pack(side=LEFT, padx=10, pady=10, expand=YES, fill=X)

# определение функции для изменения списка K
def cycle( ):
     for x in range(1, 11):
          if eval(F1.get()) <= 10:
               K[eval(F1.get())] += K[x]
          if eval(F2.get()) <= 10:
               K[eval(F2.get())] += K[x]

root.mainloop()
