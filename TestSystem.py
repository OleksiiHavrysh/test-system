from tkinter import *
from array import *
from PIL import ImageTk, Image
file = open("input.txt", 'r')
#pip install pillow 

page = Tk()
page.title("Тестирующая система")
page.geometry("500x400")
page.configure(bg = 'grey')
number = int(file.readline().rstrip("\n"))
typeofans = "1"
flag = False
j = 0
atleastonce = False
numofans = int(0)

nextButton = Button(page, text = "Следующий вопрос", background="#555", foreground="white")
previousButton = Button(page, text = "Предыдущий вопрос", background="#555", foreground="white")
nextButton.place(x = 300, y = 300)
previousButton.place(x = 100, y = 300)


labelQuestion = Label(page, text = "", font = ('Helvetica', 14, 'bold'))
while j < number:

	
	j += 1

	active = IntVar();
	active.set(0);
	numofans = int(file.readline().rstrip("\n"))
	typeofans = str(file.readline().rstrip("\n"))
	Question = str(file.readline().rstrip("\n"))
	Question = Question.rstrip("\n")
	i = 0
	Answers = []
	for i in range(numofans):
		Answers.append(str(file.readline().rstrip("\n")))
		Answers[i] = Answers[i].rstrip("\n")
	radiobuttons = []
	checkbuttons = []
	images = []
	i = 0
	if typeofans == '1':
		for i in range(numofans):
			radiobuttons.append(Radiobutton(page, text = Answers[i], variable = active, value = 0, font = ('Helvetica', 14)))
			radiobuttons[i].place(x = 0, y = 50+i*250/numofans)
	if typeofans == '2':
		for i in range(numofans):
			checkbuttons.append(Checkbutton(page, text = Answers[i], font = ('Helvetica', 14)))
			checkbuttons[i].place(x = 0, y = 50+i*250/numofans)
	if typeofans == '3':
		for i in range(numofans):
			images.append(ImageTk.PhotoImage(Image.open(Answers[i])))
			panel = Label(page, image = images[i], width = 10, height = 10)
			panel.pack(side = LEFT, fill = "both", expand = "yes")

	labelQuestion.config(text=Question)

	labelQuestion.pack(side = TOP)

page.mainloop()
