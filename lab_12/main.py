import packages
from tkinter import *

def oboi():
    window = Toplevel()
    window.title("Рассчет стоимости обоев")
    window.geometry("500x550")

    room = Label(window, text="Введите площадь комнаты (кв.м):")
    room.pack(pady=1)
    enroom = Entry(window)
    enroom.pack(pady=10)

    oboi = Label(window, text="Введите площадь одного рулона обоев (кв.м):")
    oboi.pack(pady=1)
    enoboi = Entry(window)
    enoboi.pack(pady=10)

    price = Label(window, text="Введите цену за рулон:")
    price.pack(pady=1)
    enprice = Entry(window)
    enprice.pack(pady=10)

def plitka():
    window = Tk()
    window.title("Рассчет стоимсоти плитки")
    window.geometry("500x550")

def laminat():
    window = Tk()
    window.title("Рассчет стоимсоти ламината")
    window.geometry("500x550")

def main():
    root = Tk() 
    root.title("Отделочные материалы")
    root.geometry("500x550")    

    btn1 = Button(text="Обои", command=oboi) 
    btn1.pack(fill=BOTH, expand=True)

    btn2 = Button(text="Плитка", command=plitka) 
    btn2.pack(fill=BOTH, expand=True)

    btn3 = Button(text="Ламинат", command=laminat) 
    btn3.pack(fill=BOTH, expand=True)
    root.mainloop()

main()
