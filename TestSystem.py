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

atleastonce = False
numofans = int(0)




labelQuestion = Label(page, text = "", font = ('Helvetica', 14, 'bold'))

rows, cols = (11, 11) 

radiobuttons = [[]*cols]*rows
checkbuttons = [[]*cols]*rows
images = [[]*cols]*rows
numRad = 0
numCheck = 0
numImg = 0

prev = -1
j = int(0)
'''
def Increm():
    j -= 1
'''
nextButton = Button(page, text = "Следующий вопрос", background="#555", foreground="white")
#, command = Increm()
previousButton = Button(page, text = "Предыдущий вопрос", background="#555", foreground="white")
nextButton.place(x = 300, y = 300)
previousButton.place(x = 100, y = 300)

while j < number:

    if j == prev:
        j += 1
        continue
    else: 
        prev = j
        j += 1
    active = IntVar();
	#active.set(0);
    numofans = int(file.readline().rstrip("\n"))
    typeofans = str(file.readline().rstrip("\n"))
    Question = str(file.readline().rstrip("\n"))
    Question = Question.rstrip("\n")
    i = 0
    Answers = []
    for i in range(numofans):
	    Answers.append(str(file.readline().rstrip("\n")))
	    Answers[i] = Answers[i].rstrip("\n")
	
    i = 0
    if typeofans == '1':
        numRad = 0
        for i in range(numofans):
            numRad += 1
            radiobuttons[j].append(Radiobutton(page, text = Answers[i], variable = active, value = j*10+numRad, font = ('Helvetica', 14)))
            radiobuttons[j][i].place(x = 0, y = 50+i*250/numofans)
    if typeofans == '2':
        numCheck = 0
        for i in range(numofans):
            numCheck += 1
            checkbuttons[j].append(Checkbutton(page, text = Answers[i], font = ('Helvetica', 14)))
            checkbuttons[j][i].place(x = 0, y = 50+i*250/numofans)
    if typeofans == '3':
        numImg = 0
        for i in range(numofans):
            numImg += 1
            images.append(ImageTk.PhotoImage(Image.open(Answers[i])))
            panel = Label(page, image = images[i], width = 10, height = 10)
            panel.pack(side = LEFT, fill = "both", expand = "yes")

    labelQuestion.config(text=Question)

    labelQuestion.pack(side = TOP)

page.mainloop()
