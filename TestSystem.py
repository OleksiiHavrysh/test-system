from tkinter import *

#file = open('input.txt', 'r')


page = Tk()
page.title("Тестирующая система")
page.geometry("500x400")
page.configure(bg = 'grey')
#int number = f.read()

#for i in number:


active = IntVar();
active.set(0);

Answer1 = str("1")
Answer2 = str("2")
Answer3 = str("3")
Answer4 = str("4")
Question = "Question"

radiobutton1 = Radiobutton(page, text = Answer1, variable = active, value = 0, font = ('Helvetica', 14))
radiobutton2 = Radiobutton(page, text = Answer2, variable = active, value = 1, font = ('Helvetica', 14))
radiobutton3 = Radiobutton(page, text = Answer3, variable = active, value = 2, font = ('Helvetica', 14))
radiobutton4 = Radiobutton(page, text = Answer4, variable = active, value = 3, font = ('Helvetica', 14))
labelQuestion = Label(page, text = Question, font = ('Helvetica', 14, 'bold'))
nextButton = Button(page, text = "Следующий вопрос", background="#555", foreground="white")
previousButton = Button(page, text = "Предыдущий вопрос", background="#555", foreground="white")



labelQuestion.pack(side = TOP)
radiobutton1.place(x = 0, y = 50)
radiobutton2.place(x = 0, y = 100)
radiobutton3.place(x = 0, y = 150)
radiobutton4.place(x = 0, y = 200)
nextButton.place(x = 300, y = 300)
previousButton.place(x = 100, y = 300)
#while 

page.mainloop()