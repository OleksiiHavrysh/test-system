from tkinter import *

#file = open('input.txt', 'r')


page = Tk()
page.title("Тестирующая система")
page.geometry("500x400")
page.configure(bg = 'grey')
number = int(input())
typeofans = "1"
flag = False
i = 0
atleastonce = False


nextButton = Button(page, text = "Следующий вопрос", background="#555", foreground="white")
previousButton = Button(page, text = "Предыдущий вопрос", background="#555", foreground="white")
nextButton.place(x = 300, y = 300)
previousButton.place(x = 100, y = 300)


labelQuestion = Label(page, text = "", font = ('Helvetica', 14, 'bold'))
while i < number:

	
	i += 1

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

	checkbutton1 = Checkbutton(page, text = Answer1, font = ('Helvetica', 14))
	checkbutton2 = Checkbutton(page, text = Answer2, font = ('Helvetica', 14))
	checkbutton3 = Checkbutton(page, text = Answer3, font = ('Helvetica', 14))
	checkbutton4 = Checkbutton(page, text = Answer4, font = ('Helvetica', 14))


	

	

	if typeofans == "1":
		flag = False
		if atleastonce == False:
			atleastonce = True
		radiobutton1.place(x = 0, y = 50)
		radiobutton2.place(x = 0, y = 100)
		radiobutton3.place(x = 0, y = 150)
		radiobutton4.place(x = 0, y = 200)
	else:
		flag = True
		if atleastonce == False:
			atleastonce = True


		checkbutton1.place(x = 0, y = 50)
		checkbutton2.place(x = 0, y = 100)
		checkbutton3.place(x = 0, y = 150)
		checkbutton4.place(x = 0, y = 200)
	labelQuestion.config(text=Question)

	labelQuestion.pack(side = TOP)
	
	#while nextButton:
	#	pass

	typeofans = "2"
#while 

page.mainloop()
