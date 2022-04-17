import tkinter
from tkinter import * #imports all of tktiners widgets


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        #creates a tkinter window
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='darkgrey')

        #How to assign string variables
        self.varFname = StringVar()
        self.varLname = StringVar()

        #creates labels in this section below

        self.lblFname = Label(self.master, text = 'First Name: ', font = ('Helvetica', 16), fg = 'black', bg = 'darkgrey') #creates a First name label
        self.lblFname.grid(row = 0, column = 0, padx = (30,0), pady = (30, 0)) #paints the label onto the app
        
        self.lblLname = Label(self.master, text = 'Last Name: ', font = ('Helvetica', 16), fg = 'black', bg = 'darkgrey') #creates a Last name label
        self.lblLname.grid(row = 1, column = 0, padx = (30,0), pady = (30, 0)) #paints the label  onto the app

        self.lblDisplay = Label(self.master, text = '', font = ('Helvetica', 16), fg = 'black', bg = 'darkgrey') #creates a Display label
        self.lblDisplay.grid(row = 3, column = 1, padx = (30,0), pady = (30, 0)) #paints the text box onto the app

        #creates text boxes in this section below

        self.txtFname = Entry(self.master, text = self.varFname, font = ('Helvetica', 16), fg = 'black', bg = 'lightblue') #creates a text box
        self.txtFname.grid(row = 0, column = 1, padx = (30,0), pady = (30, 0)) #paints the text box onto the app

        self.txtLname = Entry(self.master, text = self.varLname, font = ('Helvetica', 16), fg = 'black', bg = 'lightblue') #creates a text box
        self.txtLname.grid(row = 1, column = 1, padx = (30,0), pady = (30, 0)) #paints the text box onto the app


        #creates buttons in this section below

        self.btnSubmit = Button(self.master, text = 'Submit', width = 10, height = 2, command = self.submit) #creates button
        self.btnSubmit.grid(row = 2, column = 1, padx = (0,0), pady = (30, 0), sticky = NE) #paints button

        self.btnCancel = Button(self.master, text = 'Close', width = 10, height = 2, command = self.cancel) #creates button
        self.btnCancel.grid(row = 2, column = 1, padx = (0,90), pady = (30, 0), sticky = NE) #paints button




        #Define functions
    def submit(self):
        fn = self.varFname.get()
        ln = self.varLname.get()
        self.lblDisplay.config(text = 'Hello {} {}!'.format(fn, ln)) #config() updates a display while it is active



    def cancel(self):
        self.master.destroy() #command to close window
        
        
        





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #Keeps application open until quit
