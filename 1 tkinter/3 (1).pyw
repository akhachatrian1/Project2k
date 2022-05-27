from tkinter import *
from tkinter.messagebox import *
from math import sqrt
root = Tk()
root.minsize(width=400, height=150) 
root.maxsize(width=1100, height=400)
root.title("Задание 3. Калькулятор.")

# Создаем 3 фрейма для размещения компоненты для ввода чисел x, y: fr_xy, fr_op и fr_res
fr_xy = Frame(root)
fr_xy.pack(side = TOP, expand = YES, fill = X)

# На нем размещаем две метки и два редактора для ввода чисел x, y:
lx = Label(fr_xy, text = "x = ")
lx.pack(side = LEFT, padx = 10, pady = 10)
entX = Entry(fr_xy)
entX.insert(0,0) # в редактор в позицию 0 число 0
entX.pack(side = LEFT, padx = 10, pady = 10)
# Редактор будет выбран при старте (иметь фокус ввода):
entX.focus()

ly = Label(fr_xy, text = "y = ")
ly.pack(side = LEFT, padx = 10, pady = 10)
entY = Entry(fr_xy)
entY.insert(0,0)
entY.pack(side = LEFT, padx = 10, pady = 10)

# Создание фрейма с заголовком fp_op - выбор операции:
fr_op = LabelFrame(root, text = "Операция: ")
fr_op.pack(side = LEFT, fill = X)

# Операцию будем выбирать с помощью виджета Radiobutton
oper = ['+', '-', '*', '/', 'корень квадратный из x', 'квадрат y']

# Вводим строковую переменную tkinter, ее свяжем с выбором Radiobutton
varOper = StringVar()

# Вцикле создаем 6 кнопок Radiobutton (связываем их с созданной переменной VarOpen)
for op in oper:
    Radiobutton(fr_op, text = op, variable = varOper,
                value = op).pack(side = LEFT,
                padx = 20, pady = 10)

# Устанавливаем текущее значение "+"
varOper.set(oper[0])

# Создаем 3-ий фрейм fr_res - вычисление значения и вывод результата
fr_res = Frame(root)
fr_res.pack(side = TOP, expand = YES, fill = BOTH)

# Обработчик кнопок
def OnButtonResult():
    # Защищенный блок, будем пытаться перевести текст из редактора Entry в число:
    try:
        x = float(entX.get()) # извлекаем число из 1-го редактора
    except ValueError:
        # если не получилось, выдаем сообщение и выходим:
        showerror("Ошибка заполнения", "Переменная x не является числом")
        return
    # Защищенный блок 2:
    try:
        y = float(entY.get())
    except ValueError:
        showerror("Ошибка заполнения", "Переменная y не является числом")
        return
    # В переменную op записываем выбранную операцию
    op = varOper.get()
    # Вычисляем:
    if op == '+': res = x + y
    elif op == '-': res = x - y
    elif op == '*': res = x * y
    elif op == '/':
        if y != 0:
            res = x / y
        else: res = 'NAN'
    elif op == 'корень квадратный из x':
        if x >= 0:
            res = round(sqrt(x), 3)
        else: res = 'NAN'
    elif op == 'квадрат y':
        res = y*y
    else:
        res = 'операция выбрана неправильно'
    # Вывод результата на метку:
    lres['text'] = round(res,4)
#  Обработка кнопки закончилась

# Создаем кнопку и метку, к кнопке присоединяем обработчик:
Button(fr_res, text = "=", width = 10,
       command = OnButtonResult).pack(side = LEFT,padx = 30, pady = 20)
lres = Label(fr_res, text = "", width = 10)
lres.pack(side = LEFT, padx = 30, pady = 20)

# Запуск циклв обработки сообщений
root.mainloop()
