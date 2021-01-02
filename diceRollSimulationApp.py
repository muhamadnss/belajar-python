import random #Module library for randomizing number given
from tkinter import * #Define module library for utilize GUI asset maker tools

root = Tk()
root.geometry("700x450") #Initialize size of interface

label1 = Label(root, font=("times", 200))

def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label1.config(text=f'{random.choice(number)}{random.choice(number)}')
    print("Dice has been rolled") #Give return message to console compiler
    label1.pack()

button1 = Button(root, text="Roll Your Dice", command=roll) #Build CTA to roll dice
button1.place(x=300, y=265) #Define position of button

root.mainloop()