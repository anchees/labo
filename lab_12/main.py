import tkinter as tk
from tkinter import messagebox
from packages.oboi import calculate_wallpaper
from packages.plitka import calculate_tile
from packages.laminat import calculate_laminate
from packages.save import save_doc

def calculate():
    try:
        width = float(entry_width.get())
        height = float(entry_height.get())
        length = float(entry_length.get())
        material = material_var.get()
        
        if material == "Обои":
            result = calculate_wallpaper(width, height, length)
        elif material == "Плитка":
            result = calculate_tile(width, height, length)
        elif material == "Ламинат":
            result = calculate_laminate(width, length)
        else:
            messagebox.showerror("Ошибка", "Выберите материал")
            return
        
        result_label.config(text=f"Необходимое количество: {result['quantity']} шт.\nСтоимость: {result['cost']} руб.")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числовые значения")

def save_report(format):
    try:
        width = float(entry_width.get())
        height = float(entry_height.get())
        length = float(entry_length.get())
        material = material_var.get()
        
        if material == "Обои":
            result = calculate_wallpaper(width, height, length)
        elif material == "Плитка":
            result = calculate_tile(width, height, length)
        elif material == "Ламинат":
            result = calculate_laminate(width, length)
        else:
            messagebox.showerror("Ошибка", "Выберите материал")
            return
        
        if format == "doc":
            save_doc(material, result)
            
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числовые значения")


tk_root = tk.Tk()
tk_root.title("Отделочныу материалы")

tk.Label(tk_root, text="Ширина:").grid(row=0, column=0)
tk.Label(tk_root, text="Высота:").grid(row=1, column=0)
tk.Label(tk_root, text="Длина:").grid(row=2, column=0)

tk.Label(tk_root, text="Что нужно расчитать:").grid(row=3, column=0)

entry_width = tk.Entry(tk_root)
entry_height = tk.Entry(tk_root)
entry_length = tk.Entry(tk_root)
entry_width.grid(row=0, column=1)
entry_height.grid(row=1, column=1)
entry_length.grid(row=2, column=1)

material_var = tk.StringVar(value="Обои")
materials_menu = tk.OptionMenu(tk_root, material_var, "Обои", "Плитка", "Ламинат")
materials_menu.grid(row=3, column=1)

tk.Button(tk_root, text="Рассчитать", command=calculate).grid(row=4, column=0, columnspan=2)
result_label = tk.Label(tk_root, text="")
result_label.grid(row=5, column=0, columnspan=2)

tk.Button(tk_root, text="Сохранить в DOC", command=lambda: save_report("doc")).grid(row=6, column=0)

tk_root.mainloop()
