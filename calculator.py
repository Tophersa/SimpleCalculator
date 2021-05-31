# Simple basic calculator
# Mukhotho Vhonani Christopher
# 15 May 2021

from tkinter import *

window = Tk()
window.title('Calculator')

listOfNo = []

def numInput(num):
    currentValue = monitor.get()
    monitor.delete(0, END)
    monitor.insert(0, str(currentValue)+ str(num))

def clearValue():
    listOfNo.clear()
    monitor.delete(0, END)

def sumOfValues():
    no1 = monitor.get()
    listOfNo.append(no1)
    monitor.delete(0, END)


def equals():
    no1 = monitor.get()
    listOfNo.append(int(no1))
    monitor.delete(0, END)

    SUM = 0
    for values in listOfNo:
        SUM += int(values)

    monitor.insert(0, str(SUM))

#Row 0 - Name
name = Label(window, text='Calculator', font=('Arial', 15))
name.grid(row=0, columnspan=3)

#Row 1 - Display
monitor = Entry(window, width=16,  borderwidth=2, font=('Arial', 25))
monitor.grid(row=1, column=0, columnspan=3, padx=25, pady=10, sticky=N+E+W+S)

#Row 2 - (1-3)
num1 = Button(window, text='1', padx=30, pady=10, command= lambda: numInput(1))
num1.grid(row=2, column=0)

num2 = Button(window, text='2', padx=30, pady=10, command= lambda: numInput(2))
num2.grid(row=2, column=1)

num3 = Button(window, text='3', padx=30, pady=10, command= lambda: numInput(3))
num3.grid(row=2, column=2)

#Row 3 - (4-6)
num4 = Button(window, text='4', padx=30, pady=10, command= lambda: numInput(4))
num4.grid(row=3, column=0)

num5 = Button(window, text='5', padx=30, pady=10, command= lambda: numInput(5))
num5.grid(row=3, column=1)

num6 = Button(window, text='6', padx=30, pady=10, command= lambda: numInput(6))
num6.grid(row=3, column=2)

#Row 4 - (7-9)
num7 = Button(window, text='7', padx=30, pady=10, command= lambda: numInput(7))
num7.grid(row=4, column=0)

num8 = Button(window, text='8', padx=30, pady=10, command= lambda: numInput(8))
num8.grid(row=4, column=1)

num9 = Button(window, text='9', padx=30, pady=10, command= lambda: numInput(9))
num9.grid(row=4, column=2)

#Row 5 - (AC, 0, +)
ac = Button(window, text='AC',  padx=30, pady=10, command=clearValue)
ac.grid(row=5, column=0)

num0 = Button(window, text='0', padx=30, pady=10, command= lambda: numInput(0))
num0.grid(row=5, column=1)

add = Button(window, text='+', padx=30, pady=10, command=sumOfValues)
add.grid(row=5, column=2)

#Row 6 - (=)
add = Button(window, text='=', padx=145, pady=10, command=equals)
add.grid(row=6, columnspan=3)

#Calling window
window.mainloop()