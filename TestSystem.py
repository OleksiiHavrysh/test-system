from tkinter import *
from array import *
import random
#from PIL import ImageTk, Image
file = open("input.txt", 'r')
#pip install pillow 
trueans = open("trueans.txt", 'r')

root = Tk()
root.title("Тестирующая система")
root.geometry("500x400")
root.configure(bg = 'grey')
root.resizable(width=False, height=False)
number = int(file.readline().rstrip("\n"))
typeofans = "1"
flag = False

atleastonce = False
numofans = int(0)

score = int(0)
notend = True
firststart = True

labelQuestion = Label(root, text = "", font = ('Helvetica', 14, 'bold'))

rows, cols = (20, 11) 


prev = -1
j = int(0)

Questions = []
Answers = [[]*rows]*cols
typeofans = []
numofans = []
def input_():
	global number, numofans
	for i in range(number):
		numofans.append(int(file.readline().rstrip("\n")))
		typeofans.append(str(file.readline().rstrip("\n")))
		Questions.append(str(file.readline().rstrip("\n")))
		for j in range(numofans[i]):
			Answers[i].append(str(file.readline().rstrip("\n")))
			#Answers[i][j] = Answers[i][j].rstrip("\n")
                
		#random.shuffle(Answers[i])
	#random.shuffle(Answers)
	notend = True

input_()

def Increm():
    global j
    j += 1
    j = min (number - 1, j)
def Decrem():
    global j
    j -= 1
    j = max (0, j)
def EndTest():
    global notend
    if firststart == False:
        notend = False
        if typeofans[j] == '1':
            for i in range(numofans[j]):
                    radiobuttons[i].destroy()
        if typeofans[j] == '2':
            for i in range(numofans[j]):
                    checkbuttons[i].destroy()

        labelQuestion.destroy()
        nextButton.destroy()
        previousButton.destroy()
        endButton.destroy()
        
        
nextButton = Button(root, text = "Следующий вопрос", background="#555", foreground="white", command = lambda: Increm())
previousButton = Button(root, text = "Предыдущий вопрос", background="#555", foreground="white", command = lambda: Decrem())
endButton = Button(root, text = "Завершить тест", background="#555", foreground="white", command = lambda: EndTest())
nextButton.place(x = 320, y = 300)
previousButton.place(x = 50, y = 300)
endButton.place(x = 200, y = 300)



	

notend == False
j = 0

while notend:
    radiobuttons = []
    checkbuttons = []
    images = []
    firststart = False
    active = IntVar();
    i = 0
    if typeofans[j] == '1':
        if not firststart:
            for i in radiobuttons:
                radiobuttons[i].destroy()
        for i in range(numofans[j]):
            radiobuttons.append(Radiobutton(root, text = Answers[j][i], variable = active, value = j*10+i, font = ('Helvetica', 14)))
            radiobuttons[i].place(x = 0, y = 50+i*250/numofans[j])
    if typeofans[j] == '2':
        if not firststart:
            for i in checkbuttons:
                checkbuttons[i].destroy()
        for i in range(numofans[j]):
            checkbuttons.append(Checkbutton(root, text = Answers[j][i], font = ('Helvetica', 14)))
            checkbuttons[i].place(x = 0, y = 50+i*250/numofans[j])
    #if typeofans[j] == '3':
        #for i in range(numofans[j]):
            #images.append(ImageTk.PhotoImage(Image.open(Answers[j][i])))
            #panel = Label(root, image = images[i], width = 10, height = 10)
            #panel.pack(side = LEFT, fill = "both", expand = "yes")

    labelQuestion.config(text=Questions[j])
    labelQuestion.pack(side = TOP)
    root.mainloop()

