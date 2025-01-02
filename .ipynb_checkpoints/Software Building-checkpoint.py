from tkinter import *

soft = Tk()

label = Label(soft,text = "This is the Question that you can modify at your will")
label.grid()


def zero_printer(parameter):
	global sussy
	sussy = parameter

button = Button(soft,text = "You may click this to get a 0 after this box",command = lambda : zero_printer(0))
button.grid()

label2 = Label(soft,text = f"your result that is 0 ")
label2.gird()

soft.mainloop()

if __name__ == "__main__":
	soft
