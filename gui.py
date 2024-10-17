from tkinter import * #import all from tkinter GUI library
class Window(Frame):  #create Window class, inherit from Frame in tkinter
    def __init__ (self, master=None):
        self.servicelevel = DoubleVar(value=.18) #create tkinter integer for service level
        self.billAmountText = StringVar() #create tkinter string for bill amount
        self.tipAmountText = StringVar() #create tkinter string for tip amount
        Frame.__init__(self, master)
        self.master = master #master refers to the tk window
        self.init_window()  
    def init_window(self): #create and set window items
        self.master.title ("Tip Calculator") #set window title
        self.pack(fill=BOTH,expand=True) #set to fill entire window area
        menu = Menu(self.master) #create a Menu object
        self.master.config(menu=menu) #set menu instance
        file = Menu(menu) #create File menu
        file.add_command(label = "Exit", command=self.client_exit) #add	Exit command to File menu
        menu.add_cascade(label ="File",menu=file) #add to main menu
        billAmountLabel = Label(self,text="Bill Amount") #add Bill Amount label
        billAmountLabel.place(x=50,y=50)
        billAmountEntry = Entry(self,textvariable=self.billAmountText) #add Bill Amount text entry box and bind to bilAmountText
        billAmountEntry.place(x=50,y=50)
        serviceLevelLabel = Label(self,text="Service Level") #add Service Level label
        serviceLevelLabel.place(x=50,y=80)
        sll=Radiobutton(self,text="Poor",variable=self.servicelevel,value=.12) #create Service Level buttons
        sll.place(x=150,y=80)
        sl2=Radiobutton(self,text="Good",variable=self.servicelevel,value=.18)
        sl2.place(x=150,y=100)
        sl3=Radiobutton(self,text="Excellent",variable=self.servicelevel,value=.20)
        sl3.place(x=150,y=120)
        tipAmountLabel = Label(self,text="Tip Amount") #add Tip Amount label
        tipAmountLabel.place(x=50,y=180)
        tipAmountEntry = Entry(self,textvariable=self.tipAmountText) #add Tip Amount text entry box and bind to tipAmountText
        tipAmountEntry.place(x=150,y=180)
        calcButton = Button(self,text = "Calculate Tip",command=self.calcTip) #create calculate button
        calcButton.place(x=100,y=250)
        quitButton = Button(self,text = "Exit",command=self.client_exit) #create exit button and assign to quit function
        quitButton.place(x=300,y=250)
    def calcTip(self): #handles the Calculate Tip Button
        tipAmount = float(self.billAmountText.get()) * float(self.servicelevel.get()) #calculate tip
        self.tipAmountText.set(str("${:,.2f}").format(tipAmount)) #display tip formatted as currency ($ with 2 decimal places)
    def client_exit(self): #handles the Exit button and menu option
        exit() #exit program

 #main program
root = Tk()   #create new Tk object
root.geometry("400x300") #set window size
app = Window(root) #create app window
root.mainloop() #run mainloop to handle events