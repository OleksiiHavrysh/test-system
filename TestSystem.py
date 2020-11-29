import sys
from tkinter import *
from tkinter import ttk, IntVar
from array import *
import random
# from PIL import ImageTk, Image
from PySide2.QtWidgets import *

file = open("input.txt", 'r', encoding="utf8")
# pip install pillow
trueans = open("trueans.txt", 'r', encoding="utf8")

win = Tk()
win.title("Тестувальна система")
win.geometry("500x400")
win.resizable(width=False, height=False)

wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT, fill="both", expand="yes")

yscrollbar = Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0, 0), window=myframe, anchor="nw")

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="y", expand="no", padx=0, pady=15)

rows, cols = (20, 11)
number = int(file.readline().rstrip("\n"))
score = int(0)
Questions = []

Answers = []
typeofans = []
numofans = []
selected = [[] for i in range(50)]

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


def CheckUp(i, j):
    checkup[i][j] = (checkup[i][j] + 1) % 2


checkup = [[0] * 20] * 20


def count():
    global score, selected
    answer = [[] for i in range(number)]
    real = [[] for i in range(number)]

    for i in range(number):
        for j in Answers1[i]:
            real[i].append(j)

    '''for i in range(number):
        for j in range(numofans[i]):
            if active.get() == j:
                answer[i].add(radiobuttons[i][j].cget("text"))'''
    '''for k in myframe.winfo_children():
            print(radiobuttons[i][j].cget("text"))
            if k.winfo_class() == "TRadiobutton" and k.instate(['selected']) is True:
                    answer[i].add(radiobuttons[i][j].cget("text"))
                    print(radiobuttons[i][j].cget("text"))'''
    print(active.get())
    if typeofans[number - 1] == '1':
        if active.get() - (number - 1) * 20 >= 0:
            selected[number-1].append(radiobuttons[number - 1][active.get() - (number - 1) * 20].cget("text"))
    else:
        for j in checkbuttons[number - 1]:
            if CheckSelected(j) == 1:
                selected[number-1].append(j.cget("text"))
    print(answer)
    print(real)
    print(selected)
    for i in range(number):
        selected[i].sort()
        real[i].sort()

    for i in range(number):
        if selected[i] == real[i]:
            score += 1
    label = Label(win, text="Очків: " + str(score) + "/" + str(number)+"\nБалів: " + str(float((score/number)*12)), font=('Helvetica', 20, 'bold'))
    label.pack(anchor='center')


def EndTest():
    count()
    wrapper1.destroy()
    wrapper2.destroy()
    endButton.destroy()
    Next.destroy()


endButton = Button(win, text="Завершити тест", background="#555", foreground="white", command=lambda: EndTest())
endButton.place(x=200, y=370)

radioup = [0] * 10000

real = [set() for i in range(number)]

for i in range(number):
    for j in Answers1[i]:
        real[i].add(j)

id = int(0)


def Next():
    global id, score, selected
    if id >= number - 1:
        return
    if typeofans[id] == "1":
        selected[id].append(radiobuttons[id][active.get() - (id) * 20].cget("text"))

    else:
        for j in checkbuttons[id]:
            if CheckSelected(j):
                selected[id].append(j.cget("text"))
    if id < number - 1:
        main(id + 1)


Next = Button(win, text="Next", background="#555", foreground="white", command=Next)
Next.place(x=100, y=370)


def CheckSelected(check):
    return check.instate(['selected'])


def main(i):
    global id
    if i == number:
        return
    labelQuestion.append(Label(myframe, text=str(i + 1) + ". " + Questions[i], font=('Helvetica', 10, 'bold')))
    labelQuestion[i].pack(anchor=NW)

    global active, score
    active = IntVar()

    radio = []
    check = []
    img = []
    for j in range(numofans[i]):
        if typeofans[i] == "1":
            # print(j+1)
            active.set(j)
            radio.append(
                Radiobutton(myframe, text=Answers[i][j], variable=active, value=i * 20 + j))
            radio[j].pack(anchor=NW)
        if typeofans[i] == "2":
            check.append(ttk.Checkbutton(myframe, text=Answers[i][j]))
            check[j].pack(anchor=NW)

        '''if typeofans[j] == '3':
            img.append(ImageTk.PhotoImage(Image.open(Answers[j][i])))
            panel = Label(win, image = images[j], width = 10, height = 10)
            panel.pack(side = LEFT, fill = "both", expand = "yes")'''
    images.append(img)
    radiobuttons.append(radio)
    checkbuttons.append(check)
    id = i
    win.update()
    mycanvas.configure(scrollregion=mycanvas.bbox("all"))


main(0)

win.mainloop()
