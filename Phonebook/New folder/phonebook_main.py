
#tkiner imports
from tkinter import *
import tkinter as tk
from tkinter import messagebox

#other modules
import phonebook_gui
import phonebook_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        #Defines master frame config
        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)
        #Centers app on user screen
        phonebook_func.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg='#F0F0F0')
        #Built in tkinter method to catch if the user
        #clicks the upper corner, "X" on the windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a seperate module,
        #keeping code comparmentalized
        phonebook_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
