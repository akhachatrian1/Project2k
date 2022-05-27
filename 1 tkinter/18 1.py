from tkinter import *

root = Tk()

#обозначаем размер
root.minsize(width = 350, height = 150)
root.maxsize(width = 500, height = 300)
root.title("Основное окно")

#команда совершаемая после нажатия на кнопку в доп окне
def writeText():
    print("hello")
    

#создаем новое окно с помощью Toplevel
def newWindow():
    window = Toplevel(root)
    window.geometry('300x100+100+100')
 #задаем размер
    Button(window,text="кнопка",command=writeText).pack(side=BOTTOM, padx=10, pady=5)
    Label(window,text="нажмите").pack(side=BOTTOM, padx=10, pady=5)

button = Button(root, text="Дополнительное окно", command=newWindow).pack(side=BOTTOM, padx=10, pady=5)

root.mainloop()

