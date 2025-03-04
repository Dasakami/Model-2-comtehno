import os
import tkinter as tk
from tkinter import messagebox

FILE_NAME = "students.txt"

def read_students():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            students = [line.strip().split(", ") for line in file.readlines()]
        return [(name, float(grade)) for name, grade in students]
    except FileNotFoundError:
        return []
    except ValueError:
        messagebox.showerror("Ошибка", "Ошибка в формате данных файла!")
        return []

def write_students(students):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for name, grade in students:
                file.write(f"{name}, {grade}\n")
    except PermissionError:
        messagebox.showerror("Ошибка", "Нет прав на запись в файл!")

def list_students():
    students = read_students()
    text_output.delete("1.0", tk.END)  
    if not students:
        text_output.insert(tk.END, "Список пуст или файл отсутствует.\n")
    else:
        for name, grade in students:
            text_output.insert(tk.END, f"{name}, {grade}\n")

def add_student():
    name = entry_name.get().strip()
    try:
        grade = float(entry_grade.get().strip())
        students = read_students()
        students.append((name, grade))
        write_students(students)
        list_students()
        messagebox.showinfo("Успех", "Студент добавлен!")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число для балла!")

def delete_student():
    name = entry_name.get().strip()
    students = read_students()
    new_students = [s for s in students if s[0] != name]
    if len(new_students) == len(students):
        messagebox.showwarning("Ошибка", "Студент не найден!")
    else:
        write_students(new_students)
        list_students()
        messagebox.showinfo("Успех", "Студент удалён!")

def find_best_student():
    students = read_students()
    if not students:
        messagebox.showwarning("Ошибка", "Список студентов пуст.")
        return
    best_student = max(students, key=lambda s: s[1])
    messagebox.showinfo("Лучший студент", f"{best_student[0]} ({best_student[1]})")

def update_grade():
    name = entry_name.get().strip()
    students = read_students()
    for i, (student_name, grade) in enumerate(students):
        if student_name == name:
            try:
                new_grade = float(entry_grade.get().strip())
                students[i] = (name, new_grade)
                write_students(students)
                list_students()
                messagebox.showinfo("Успех", "Средний балл обновлён!")
                return
            except ValueError:
                messagebox.showerror("Ошибка", "Введите корректное число!")
                return
    messagebox.showwarning("Ошибка", "Студент не найден!")

root = tk.Tk()
root.title("Управление студентами")
root.geometry("500x400")
root.resizable(False, False)

tk.Label(root, text="Имя студента:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root, font=("Arial", 12), width=20)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Средний балл:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_grade = tk.Entry(root, font=("Arial", 12), width=20)
entry_grade.grid(row=1, column=1, padx=10, pady=5)

btn_list = tk.Button(root, text="Список студентов", font=("Arial", 10), command=list_students, width=18)
btn_list.grid(row=2, column=0, padx=5, pady=5)

btn_add = tk.Button(root, text="Добавить", font=("Arial", 10), command=add_student, width=18)
btn_add.grid(row=2, column=1, padx=5, pady=5)

btn_delete = tk.Button(root, text="Удалить", font=("Arial", 10), command=delete_student, width=18)
btn_delete.grid(row=3, column=0, padx=5, pady=5)

btn_update = tk.Button(root, text="Изменить балл", font=("Arial", 10), command=update_grade, width=18)
btn_update.grid(row=3, column=1, padx=5, pady=5)

btn_best = tk.Button(root, text="Лучший студент", font=("Arial", 10), command=find_best_student, width=18)
btn_best.grid(row=4, column=0, padx=5, pady=5)

btn_exit = tk.Button(root, text="Выход", font=("Arial", 10), command=root.quit, width=18)
btn_exit.grid(row=4, column=1, padx=5, pady=5)

text_output = tk.Text(root, font=("Arial", 12), width=50, height=10)
text_output.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
