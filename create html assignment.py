import webbrowser
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox


bodyText = 'Stay tuned for our amazing summer sale!!'




class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #Defines master frame size
        self.master = master
        self.master.minsize(380, 220)
        self.master.maxsize(380, 220)
        #sets background color
        self.master.configure(bg = '#000000')
        #title
        self.master.title("HTML WEB TEXT UPDATER")
        #confirms user wants to quit
        self.master.protocol("WM_DELETE_WINDOW", lambda:ask_quit(self))
        arg = self.master

        #loads gui
        load_gui(self)


#########################################################################################################################################
        #MAKING GUI ELEMENTS



#all the elements for the gui are in this function
def load_gui(self):
    #label for new html
    self.lbl1 = tk.Label(self.master, text = "Updated Text for HTML File", fg = "yellow", bg = 'black')
    self.lbl1.grid(row = 0, column = 0, padx = 10)
    #text box for inputing updates h1 tag
    self.txt = Text(self.master, height = 10, width = 20, bg = 'White')
    self.txt.grid(row = 1, column = 0)
    #Update and close buttons
    self.upd = tk.Button(self.master, text = 'Update', bg = 'white', command = lambda: update_html(self))
    self.upd.grid(row = 2, column = 0, padx = 20)
    self.close = tk.Button(self.master, text = 'Open HTML', bg = 'white', command = lambda: openFile)
    self.close.grid(row = 2, column = 1, padx = 20)
    #label for current html
    self.lbl2 = tk.Label(self.master, text = "Current Text for HTML File", fg = "yellow", bg = 'black')
    self.lbl2.grid(row = 0, column = 1, padx = 10)
    #Text that displays what the current H1 tag says
    self.list = Text(self.master, height = 10, width = 20, bg = 'White')
    self.list.grid(row = 1, column = 1, padx = 20)
    self.list.insert('end', bodyText)
    self.list.config(state = 'disabled')



#########################################################################################################################################
    #APPLICATION FUNCTIONS

#updates html h1 tag to what is in txt element
def update_html(self):
    bodyText = self.txt.get('1.0', END)
    self.list.config(state = 'normal')
    self.list.delete('1.0', 'end')
    self.txt.delete('1.0', 'end')
    self.list.insert('end', bodyText)
    self.list.config(state = 'disabled')
    print(bodyText)
    f = open('index.html', 'a')
    htmlText = ("""
            <html>
                <body>
                    <h1>{}</h1>
                </body>
            </html>
            """).format(bodyText)
    f.write(htmlText)
    f.close()



    
    
    



#Makes sure user wants to exit program if they click on 'X' in upper right
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)



########################################################################################################################################
        #FUNCTIONS FOR MAKING ORGINAL FILE

#creates function for making HTML file
def createFile():
   f = open('index.html', 'w')
   f.write("""
            <html>
                <body>
                    <h1>{}</h1>
                </body>
            </html>
            """).format(bodyText)
   f.close()

#function for opening file in browser
def openFile():
    webbrowser.open_new_tab('C:\Tech Academy Projects\Python_Projects\Python-Projects\index.html')

#######################################################################################################################################

if __name__ == '__main__':
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()
