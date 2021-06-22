from tkinter import *
from PIL import Image, ImageTk

tk=Tk()
tk.title("Ядерный реактор Брянска модели BR-41245")
tk.geometry("600x140")
tk.resizable(False, False)
canvas = Canvas(tk, height=450, width=600)
image = Image.open("D:\\zest.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, -150, anchor='nw',image=photo)
canvas.grid(row=2,column=1)
l1=Label(text="Программа по управлению ядерным реактором Брянска",bg='white')
l1.place(x=0,y=0)
nap = 500
def bryansk(): print("Реактор взорван!")
b1 = Button(text="Взорвать реактор",command=bryansk)
b1.place(x=0,y=35)
def ku():
	global nap;nap+=100;print(f"Напряжение повышено до {nap}МВ!")
	if nap == 1000: print("Реактор взорвался")
b2 = Button(text="Повысить напряжение",command=ku)
b2.place(x=0,y=70)
def re():
	global nap;nap-=100;print(f"Напряжение понижено до {nap}МВ!")
	if nap == 0: print("Реактор взорвался от недостатка напряжения")
b3 = Button(text="Понизить напряжение",command=re)

b3.place(x=0,y=105)

tk.mainloop()
