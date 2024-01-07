import tkinter 
from tkinter import *
import random
root = tkinter.Tk()
root.title("rock paper scissor game")
root.configure(background="blue")
root.geometry("800x300")
root.resizable(width=False,height=False)
#code
r = ['rock', 'paper', 'scissor']

rock_image = """
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)"""

paper_image = """
     ___
---'    _)_
           __)
          ___)
         ___)
---.____)"""

scissor_image = """
    ___
---'   _)_
          __)   
       ____)   
      (__)
---._(__)"""

#reset function
def reset():
    global random_choice
    r = ['rock', 'paper', 'scissor']
    random_choice = random.choice(r)
    f=open("score.txt",'w')
    f.write("highest score: ")
    f.write(str(label_userscore['text']))
    f.close()


    label_computer['text'] = scissor_image
    label_user['text'] = paper_image
    label_result['text'] = "Choose...."
    label_computerscore['text']=0
    label_userscore['text']=0

#checking rock function
def rock():
    label_user['text'] = rock_image
    random_choice = random.choice(r)

    if random_choice == "rock":
        label_result['text'] = "TIE"
        label_computer['text'] = rock_image
    elif random_choice == "paper":
        label_result['text'] = "COMPUTER WINS!!"
        label_computer['text'] = paper_image
    elif random_choice == "scissor":
        label_result['text'] = "USER WINS!!"
        label_computer['text'] = scissor_image

#checking paper function
def paper():
    label_user['text'] = paper_image
    random_choice = random.choice(r)

    if random_choice == "paper":
        label_result['text'] = "TIE"
        label_computer['text'] = paper_image
    elif random_choice == "scissor":
        label_result['text'] = "COMPUTER WINS!!"
        label_computer['text'] = scissor_image
    elif random_choice == "rock":
        label_result['text'] = "USER WINS!!"
        label_computer['text'] = rock_image

#checking scissor function
def scissor():
    label_user['text'] = scissor_image
    random_choice = random.choice(r)

    if random_choice == "scissor":
        label_result['text'] = "TIE"
        label_computer['text'] = scissor_image
    elif random_choice == "rock":
        label_result['text'] = "COMPUTER WINS!!"
        label_computer['text'] = rock_image
    elif random_choice == "paper":
        label_result['text'] = "USER WINS!!"
        label_computer['text'] = paper_image

#score update function
def update():

    if label_user['text'] == paper_image:
        if label_computer['text'] == paper_image:
            label_userscore['text']+=0
            label_computerscore['text']+=0
        elif label_computer['text'] == scissor_image:
            label_computerscore['text']+=1
            label_userscore['text']+=0
        elif label_computer['text'] == rock_image:
            label_computerscore['text']+=0
            label_userscore['text']+=1

    if label_user['text'] == rock_image:
        if label_computer['text'] == rock_image:
            label_userscore['text']+=0
            label_computerscore['text']+=0
        elif label_computer['text'] == paper_image:
            label_computerscore['text']+=1
            label_userscore['text']+=0
        elif label_computer['text'] == scissor_image:
            label_computerscore['text']+=0
            label_userscore['text']+=1

    if label_user['text'] == scissor_image:
        if label_computer['text'] == scissor_image:
            label_userscore['text']+=0
            label_computerscore['text']+=0
        elif label_computer['text'] == rock_image:
            label_computerscore['text']+=1
            label_userscore['text']+=0
        elif label_computer['text'] == paper_image:
            label_computerscore['text']+=0
            label_userscore['text']+=1




#button for choosing
button_rock = Button(root, text="Rock", command=lambda: [rock(), update()],width=15,bg="#F4C430")
button_rock.grid(row=5, column=2)

button_paper = Button(root, text="Paper", command=lambda: [paper(), update()],width=15,bg="white")
button_paper.grid(row=5, column=3)

button_scissors = Button(root, text="Scissors", command=lambda: [scissor(), update()],width=15,bg="green")
button_scissors.grid(row=5, column=4)

#label for showing
label_computer = Label(root, justify=tkinter.LEFT, font="Courier", text=paper_image,width=15,height=8,bg="blue",fg="#E8BEAC")
label_computer.grid(row=2, column=1)

label_user = Label(root, justify=tkinter.LEFT, font="Courier", text=scissor_image,width=15,height=8,bg="blue",fg="#E8BEAC")
label_user.grid(row=2, column=5)

#label for detailing
label_user1=Label(root,text="User",bg="blue",fg="white",font="none 16 bold")
label_user1.grid(row=1,column=4)

label_computer1=Label(root,text="Computer",bg="blue",fg="white",font="none 16 bold")
label_computer1.grid(row=1,column=2)

label_userscore=Label(root,text=0,bg="blue",fg="white",font="none 12 bold")
label_userscore.grid(row=2,column=4)

label_computerscore=Label(root,text=0,bg="blue",fg="white",font="none 12 bold")
label_computerscore.grid(row=2,column=2)

#label for result
label_result = Label(root, text="Choose...",bg="blue",fg="yellow",width=14,font="none 16 bold")
label_result.grid(row=6, column=3)

#button for reset
button_reset = Button(root, text="Reset", command=reset,bg="red",width=15)
button_reset.grid(row=7, column=3)


root.mainloop()
