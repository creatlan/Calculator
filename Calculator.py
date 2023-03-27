import tkinter as tk
from math import *


def true_or_float():
    value = calc.get()
    if value[-1] == '.':
        return True
    return False


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:  # and true_or_float() == 'True':
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + str(digit))


def add_operation(operation):
    value = '0000000' + calc.get()
    if value[-1] in '+, -, *, /, .':
        value = value[:-1]
    elif value[-2] in 'pe, e':
        value = value[:-2]
    value = value[7::]
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)


def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value+value[:-1]
        first_calc = eval(value)
    else:
        first_calc = eval(value)
    if first_calc == round(first_calc):
        first_calc = round(first_calc)
    calc.delete(0, tk.END)
    calc.insert(0, first_calc)


def trigonometry(operation):
    if operation == 'sin':
        first_calc = sin(float(calc.get()) / 57.3)
    elif operation == 'cos':
        first_calc = cos(float(calc.get()) / 57.3)
    elif operation == 'tg':
        first_calc = tan(float(calc.get()) / 57.3)
    elif operation == 'ctg':
        first_calc = 1/tan(float(calc.get())/57.3)
    calc.delete(0, tk.END)
    calc.insert(0, first_calc)


def zero():
    calc.delete(0, tk.END)
    calc.insert(0, 0)


def make_digit_button(digit):
    return tk.Button(win, text=digit, bd=3, bg='#EFECEC', command=lambda: add_digit(digit), font=('Arial', 13))


def make_operation_button(operation):
    return tk.Button(win, text=operation, bd=3, bg='#D0B4B4', command=lambda: add_operation(operation), font=('Arial', 13))


def make_zero_button(operation):
    return tk.Button(win, text=operation, bd=3, bg='#D0B4B4', command=zero, font=('Arial', 13))


def make_calc_button(operation):
    return tk.Button(win, text=operation, bd=3, bg='#D0B4B4', command=calculate, font=('Arial', 13))


win = tk.Tk()
win.geometry("425x330+500+350")
win.config(bg='#7C5858')
win.title('Калькулятор')


calc = tk.Entry(win, justify=tk.RIGHT,
                width=20,
                font=('Arial', 15),
                relief=tk.RAISED,
                bd=4,
                )
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=7, stick='we', padx=5, pady=5)


make_digit_button(1).grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button(2).grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_digit_button(3).grid(row=1, column=4, stick='wens', padx=5, pady=5)
make_digit_button(4).grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button(5).grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_digit_button(6).grid(row=2, column=4, stick='wens', padx=5, pady=5)
make_digit_button(7).grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button(8).grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_digit_button(9).grid(row=3, column=4, stick='wens', padx=5, pady=5)
make_digit_button(0).grid(row=4, column=2, stick='wens', padx=5, pady=5, columnspan=2)
tk.Button(win, text='.', bd=3, bg='#EFECEC', command=lambda: calc.insert('end', '.'), font=('Arial', 13)).grid(row=4, column=4, stick='wens', padx=5, pady=5)


tk.Button(win, text='sin', bd=3, bg='#D0B4B4', command=lambda: trigonometry('sin'), font=('Arial', 13)).grid(row=1, column=0, stick='wens', padx=5, pady=5, columnspan=2)
tk.Button(win, text='cos', bd=3, bg='#D0B4B4', command=lambda: trigonometry('cos'), font=('Arial', 13)).grid(row=2, column=0, stick='wens', padx=5, pady=5, columnspan=2)
tk.Button(win, text='tg', bd=3, bg='#D0B4B4', command=lambda: trigonometry('tg'), font=('Arial', 13)).grid(row=3, column=0, stick='wens', padx=5, pady=5, columnspan=2)
tk.Button(win, text='ctg', bd=3, bg='#D0B4B4', command=lambda: trigonometry('ctg'), font=('Arial', 13)).grid(row=4, column=0, stick='wens', padx=5, pady=5, columnspan=2)
tk.Button(win, text='pi', bd=3, bg='#EFECEC', command=lambda: calc.insert('end', '3.14'), font=('Arial', 13)).grid(row=5, column=0, stick='wens', padx=5, pady=5)
tk.Button(win, text='e', bd=3, bg='#EFECEC', command=lambda: calc.insert('end', '2.71828'), font=('Arial', 13)).grid(row=5, column=1, stick='wens', padx=5, pady=5)
make_operation_button('+').grid(row=1, column=5, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=1, column=6, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=2, column=5, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=2, column=6, stick='wens', padx=5, pady=5)
tk.Button(win, text='√', bd=3, bg='#D0B4B4', command=lambda: calc.insert(0, float(calc.get()) ** 0.5), font=('Arial', 13)).grid(row=3, column=5, stick='wens', padx=5, pady=5)
tk.Button(win, text='!', bd=3, bg='#D0B4B4', command=lambda: calc.insert(0, factorial(int(calc.get()))), font=('Arial', 13)).grid(row=3, column=6, stick='wens', padx=5, pady=5)
make_zero_button('C').grid(row=4, column=5, stick='wens', padx=5, pady=5, columnspan=2, rowspan=2)

make_calc_button('=').grid(row=5, column=2, stick='wens', padx=5, pady=5, columnspan=3)


win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_columnconfigure(4, minsize=60)
win.grid_columnconfigure(5, minsize=60)
win.grid_columnconfigure(6, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.resizable(False, False)
win.mainloop()
