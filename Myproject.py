import time 
import random 
import tkinter as tk

time.sleep(1)
print('Вас приветствуют!')
time.sleep(1)
print('Вы должны выбрать варианты - a/b/c')

current = input(str());

if current == 'a':
    print('Вы выбрали игру блэкджэк!')
elif current == 'b':
    print('Хорошо, вы выбрали 8 бит игру')
elif current == 'c':
    print('Вы выходите из этой программы!')

def task():
    time.sleep(2)
    root.destroy()

root = tk.Tk()
root.title('GUI on Python')
root.geometry('500x500')

label = tk.Label(text='Its my code!', fg = '#eee', bg = '#333')
label.pack()

btn1 = Button(text = 'Its my code!', fg = '#333', bg = '#333')
btn1.pack()

root.after(10000, task)
root.mainloop()

print('Main loop is now over and we can do other stuff')
time.sleep(1)
print('Программа готова')