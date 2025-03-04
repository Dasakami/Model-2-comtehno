import math
import tkinter as tk
from tkinter import messagebox

def add():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result.set(a + b)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа!")

def subtract():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result.set(a - b)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа!")

def multiply():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result.set(a * b)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа!")

def divide():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно!")
        result.set(a / b)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа!")
    except ZeroDivisionError as e:
        messagebox.showerror("Ошибка", str(e))

def sqrt():
    try:
        a = float(entry1.get())
        if a < 0:
            raise ValueError("Корень из отрицательного числа не определен!")
        result.set(math.sqrt(a))
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

def factorial():
    try:
        a = int(entry1.get())
        if a < 0:
            raise ValueError("Факториал определен только для неотрицательных целых чисел!")
        result.set(math.factorial(a))
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

def percent():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result.set((a * b) / 100)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа!")

def power():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result.set(a ** b)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа!")

def sin_func():
    try:
        a = float(entry1.get())
        result.set(round(math.sin(math.radians(a)), 6))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите число!")

def cos_func():
    try:
        a = float(entry1.get())
        result.set(round(math.cos(math.radians(a)), 6))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите число!")

def tan_func():
    try:
        a = float(entry1.get())
        if (a % 180) == 90:
            raise ValueError("Тангенс 90° не определен!")
        result.set(round(math.tan(math.radians(a)), 6))
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

root = tk.Tk()
root.title("Калькулятор")
result = tk.StringVar()

tk.Label(root, text="Первое число:", font=("Arial", 14)).grid(row=0, column=0, padx=20, pady=5, sticky="w")
entry1 = tk.Entry(root, font=("Arial", 14), width=15)
entry1.grid(row=0, column=1)

tk.Label(root, text="Второе число:", font=("Arial", 14)).grid(row=1, column=0, padx=20, pady=5, sticky="w")
entry2 = tk.Entry(root, font=("Arial", 14), width=15)
entry2.grid(row=1, column=1)

tk.Label(root, text="Результат:", font=("Arial", 14)).grid(row=2, column=0, padx=20, pady=5, sticky="w")
tk.Entry(root, textvariable=result, state="readonly", font=("Arial", 14), width=15).grid(row=2, column=1)

buttons = [
    ("+", add), ("-", subtract), ("*", multiply), ("/", divide),
    ("√", sqrt), ("!", factorial), ("%", percent), ("^", power),
    ("sin", sin_func), ("cos", cos_func), ("tan", tan_func)
]

row = 3
col = 0
for text, func in buttons:
    tk.Button(root, text=text, command=func, font=("Arial", 14), width=5, height=2).grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
