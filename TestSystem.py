from tkinter import *
from tkinter import ttk
from array import *
import random
#from PIL import ImageTk, Image
file = open("input.txt", 'r')
#pip install pillow 
trueans = open("trueans.txt", 'r')

win = Tk()
win.title("Тестирующая система")
win.geometry("500x400")
win.resizable(width=False, height=False)
wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side = LEFT, fill="both", expand = "yes")

yscrollbar = Scrollbar(wrapper1, orient = "vertical", command = mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill="y")

mycanvas.configure(yscrollcommand = yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window = myframe, anchor = "nw")

wrapper1.pack(fill="both", expand="yes", padx=10,pady=10)
wrapper2.pack(fill="y", expand="no", padx=0,pady=15)

rows, cols = (20, 11)
number = int(file.readline().rstrip("\n"))
score = int(0)
Questions = []

Answers = []
typeofans = []
numofans = []



def input_():
	global number
	for i in range(number):
		numofans.append(int(file.readline().rstrip("\n")))
		typeofans.append(str(file.readline().rstrip("\n")))
		Questions.append(str(file.readline().rstrip("\n")))
		ans = []
		for j in range(numofans[i]):
				ans.append(str(file.readline().rstrip("\n")))
		random.shuffle(ans)
		Answers.append(ans)

input_()

Answers1 = []
numofans1 = []

def input_ans():
	global number
	for i in range(number):
		if typeofans[i] == "2":
			numofans1.append(int(trueans.readline().rstrip("\n")))
		else:
			numofans1.append(1)
		ans = []
		for j in range(numofans1[i]):
				ans.append(str(trueans.readline().rstrip("\n")))
		Answers1.append(ans)

input_ans()



labelQuestion = []
radiobuttons = []
checkbuttons = []
images = []

radioup = [[0]*20]*20

def RadioUp(i,j):
    radioup[i][j]=(radioup[i][j]+1)%2
def CheckUp(i,j):
    checkup[i][j]=(radioup[i][j]+1)%2
    
checkup = [[0]*20]*20


    
def count():
        global score
        answer = [set() for i in range(number)]
        real = [set() for i in range(number)]

        for i in range(number):
            for j in Answers1[i]:
                real[i].add(j)

        
        for i in range(number):
                for j in range(numofans[i]):
                        if adioup[i][j] == 1:#radiobutton[i][j].cget("text")
                                answer[i].add(Answers[i][j])
        for i in range(number):
                for j in range(numofans[i]):
                        if checkup[i][j] == 1:
                                answer[i].add(Answers[i][j])
                                
        for i in range(number):
                if answer[i] == real[i]:
                        score += 1
        label = Label(win, text = "Очки: " + str(score) + "/" + str(number), font = ('Helvetica', 20, 'bold'))
        label.place(x = 195, y = 180)
                     
def EndTest():
    count()
    wrapper1.destroy()
    wrapper2.destroy()
    endButton.destroy()

endButton = Button(win, text = "Завершить тест", background="#555", foreground="white", command = lambda: EndTest())
endButton.place(x = 200, y = 370)






for i in range(number):
        labelQuestion.append(Label(myframe, text = str(i+1)+". "+Questions[i], font = ('Helvetica', 14, 'bold')))
        labelQuestion[i].pack(anchor=NW)
        radio = []
        check = []
        img = []
        active = IntVar()
        active.set(-1)
        for j in range(numofans[i]):
                if typeofans[i] == "1":
                        radio.append(Radiobutton(myframe,text=Answers[i][j],variable=active,value=i*200+j,font=('Helvetica',14),command=lambda: RadioUp(i,j)))
                        radio[j].pack(anchor=NW)
                if typeofans[i] == "2":
                        check.append(Checkbutton(myframe, text = Answers[i][j], font = ('Helvetica', 14),command=lambda: CheckUp(i,j)))
                        check[j].pack(anchor=NW)
                        
                '''if typeofans[j] == '3':
                    for i in range(numofans[j]):
                        img.append(ImageTk.PhotoImage(Image.open(Answers[j][i])))
                        panel = Label(root, image = images[i], width = 10, height = 10)
                        panel.pack(side = LEFT, fill = "both", expand = "yes")'''
        images.append(img)
        radiobuttons.append(radio)
        checkbuttons.append(check)
        
        









win.mainloop()
