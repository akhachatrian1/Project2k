from tkinter import *
import random
from tkinter.messagebox import *

sum = 5
ent_b = [0]*sum
a = 0

root = Tk()
root.minsize(width = 250, height = 350)
root.title("Сумма")

win = Frame(root)
win.pack(expand = True)

for i in range (sum):
     Label(win, text = "x" + str(i+1) + " = ").grid(row = i, column = 0)
     ent_b[i] = Entry(win)
     ent_b[i].grid(row = i, column = 1)
     ent_b[i].insert(0, str(random.randint(0, 10)))


Button(win, text = 'Вычислить', command=res).grid(row = sum, column = 0)

ent_s = Entry(win)
ent_s.grid(row = sum, column = 1)
res()

root.mainloop( )
