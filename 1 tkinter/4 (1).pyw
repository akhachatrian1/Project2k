from tkinter import *
from math import *   
from tkinter.messagebox import *

root  =  Tk( )
root.title("Вычисление функции:")
root.config(bg = 'pink')

#  создаем Frame для размещения компонент задающих x:
win1  =  Frame(root)
win1.config(bg = 'pink')
win1.pack(anchor  =  "n", expand  =  YES, fill  =  X)

lx  =  Label(win1,  text  =  "x = ")
lx.config(font = ('Helvetica', 10))
lx.config(bg = 'pink')
lx.pack(side  =  LEFT,  padx  =  40)
entX  =  Entry(win1)
entX.insert(0, 0)
entX.pack(side   =  LEFT,  padx  = 10)
entX.focus(  )

# создаем второй Frame для задания функции и вычисления:
win2  =  Frame(root)
win2.config(bg = 'pink')
win2.pack(anchor  =  "n", expand  =  YES, fill  =  X)
Label(win2,  text  =  "Функция: ", font = ('Helvetica', 10)).pack(side  =  LEFT, padx  =  10)
entF   =  Entry(win2)
entF.pack(side   =  LEFT, padx  =  5, expand  =  YES, fill  =  X)
entF.insert(0, "sin(pi*(x*x-x-2))/(cos(pi*x)+1)")

# Создаем обработчик кнопки: 
def  res( ): 
     try: 
          x   =   int(entX.get()) 
     except ValueError:
          showerror("Ошибка заполнения", "Переменная x не является целым числом")
          return
     F = entF.get( )  # считываем текст из редактора
     if (cos(pi * x) == -1):
         showerror("Ошибка выполнения","Деление на ноль")
     else:
         labF['text']  =  eval(F) # выполняем его и результат
    # записываем на метку

# Создаем кнопку и метку:
Button(win2, text = 'Вычислить', command  =  res, font = ('Helvetica', 10)).pack(side  =  LEFT, padx  =  10)
labF  =  Label(win2,  text  =  " ")
labF.pack(side  =  LEFT,  padx  =  10)
root.mainloop()
