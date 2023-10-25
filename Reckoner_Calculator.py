#################################################################
# Name: Zoe Baker
# Date: 2/2/23
# Description: A GUI calculator based in tkinter
#################################################################
from tkinter import *

# the main GUI
class MainGUI(Frame):
    global enterHit
    enterHit = False
    #constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        self.setupGUI()
    
    #sets up GUI
    def setupGUI(self):
        #base label widget - right-align, white bg, height 2, width 15, font 50, fill horizontally and vertically
        self.display = Label(self, text="", anchor=E, bg="white", height=2, width=15, font=("",40))
        self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)
        
        #button widgets
        #left parenthesis
        img = PhotoImage(file="Images/lpr.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("("))
        button.image = img
        button.grid(row=1, column=0, sticky=N+S+E+W)
        
        #right parenthesis
        img = PhotoImage(file="Images/rpr.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process(")"))
        button.image = img
        button.grid(row=1, column=1, sticky=N+S+E+W)
        
        #AC
        img = PhotoImage(file="Images/clr.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("AC"))
        button.image = img
        button.grid(row=1, column=2, sticky=N+S+E+W)
        
        #two stars
        img = PhotoImage(file="Images/bak.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("back"))
        button.image = img
        button.grid(row=1, column=3, sticky=N+S+E+W)
        
        #7
        img = PhotoImage(file="Images/7.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("7"))
        button.image = img
        button.grid(row=2, column=0, sticky=N+S+E+W)
        
        #8
        img = PhotoImage(file="Images/8.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("8"))
        button.image = img
        button.grid(row=2, column=1, sticky=N+S+E+W)
        
        #9
        img = PhotoImage(file="Images/9.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("9"))
        button.image = img
        button.grid(row=2, column=2, sticky=N+S+E+W)
        
        #division
        img = PhotoImage(file="Images/div.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("/"))
        button.image = img
        button.grid(row=2, column=3, sticky=N+S+E+W)
        
        #4
        img = PhotoImage(file="Images/4.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("4"))
        button.image = img
        button.grid(row=3, column=0, sticky=N+S+E+W)
        
        #5
        img = PhotoImage(file="Images/5.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("5"))
        button.image = img
        button.grid(row=3, column=1, sticky=N+S+E+W)
        
        #6
        img = PhotoImage(file="Images/6.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("6"))
        button.image = img
        button.grid(row=3, column=2, sticky=N+S+E+W)
        
        #multiplication
        img = PhotoImage(file="Images/mul.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("*"))
        button.image = img
        button.grid(row=3, column=3, sticky=N+S+E+W)
        
        #1
        img = PhotoImage(file="Images/1.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("1"))
        button.image = img
        button.grid(row=4, column=0, sticky=N+S+E+W)
        
        #2
        img = PhotoImage(file="Images/2.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("2"))
        button.image = img
        button.grid(row=4, column=1, sticky=N+S+E+W)
        
        #3
        img = PhotoImage(file="Images/3.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("3"))
        button.image = img
        button.grid(row=4, column=2, sticky=N+S+E+W)
        
        #subtraction
        img = PhotoImage(file="Images/sub.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("-"))
        button.image = img
        button.grid(row=4, column=3, sticky=N+S+E+W)
        
        #0
        img = PhotoImage(file="Images/0.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("0"))
        button.image = img
        button.grid(row=5, column=0, sticky=N+S+E+W)
        
        #decimal
        img = PhotoImage(file="Images/dot.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("."))
        button.image = img
        button.grid(row=5, column=1, sticky=N+S+E+W)
        
        #addition
        img = PhotoImage(file="Images/add.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("+"))
        button.image = img
        button.grid(row=5, column=3, sticky=N+S+E+W)

        #equals
        img = PhotoImage(file="Images/eql-wide.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("="))
        button.image = img
        button.grid(row=6, column=0, columnspan=2, sticky=N+S+E+W)

        #power/stars
        img = PhotoImage(file="Images/pow.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("**"))
        button.image = img
        button.grid(row=6, column=2, sticky=N+S+E+W)

        #mod/%
        img = PhotoImage(file="Images/mod.gif")
        button = Button(self, bg="white", image=img, command=lambda: self.process("%"))
        button.image = img
        button.grid(row=6, column=3, sticky=N+S+E+W)
        
        #pack
        self.pack(fill=BOTH, expand=1)
    
    #process button presses
    def process(self, button):
        global enterHit
        #print(button + " button pressed")
        #clear display
        if(button == "AC"):
            enterHit = False
            self.display["text"] = ""
        #backspace
        elif(button == "back"):
            enterHit = False
            tempStr = self.display["text"]
            tempStr = tempStr[0:int(len(tempStr) - 1)]
            self.display["text"] = tempStr
        #evaluate equation
        elif (button == "="):
            enterHit = True
            expr = self.display["text"]
            try:
                result = str(eval(expr))
            except:
                result = "Error"
            length = int(len(result))
            if(length >= 14):
                result = result[0:11] + "..."
            self.display["text"] = result
        #otherwise, type
        else:
            if(enterHit):
                self.process("AC")
            tempStr = self.display["text"]
            if len(tempStr) < 14:
                self.display["text"] += button
        




##############################
# the main part of the program
##############################
# create the window
window = Tk()
# set the window title
window.title("The Reckoner")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()
