from tkinter import *

page = Tk()
page.title("Приложение")
page.geometry("700x500+100+100")

active = IntVar();
active.set(0);
Question1 = str("1")
Question2 = str("2")
Question3 = str("3")
Question4 = str("4")

radiobutton1 = Radiobutton(page, text = Question1, variable = active, value = 0)
radiobutton2 = Radiobutton(page, text = Question2, variable = active, value = 1)
radiobutton3 = Radiobutton(page, text = Question3, variable = active, value = 2)
radiobutton4 = Radiobutton(page, text = Question4, variable = active, value = 3)






radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()

page.mainloop()