import shutil
import os
from os import path
import datetime
from datetime import date, time, timedelta
import tkinter as tk
from tkinter import *
from tkinter import filedialog



class WindowMain(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('500x100')
        self.master.title('File Transfer')

        self.lblFileA = Label(self.master, text = 'File Path A: ')
        self.lblFileA.grid(row = 0, column = 0)
        self.lblFileB = Label(self.master, text = 'File Path B: ')
        self.lblFileB.grid(row = 0, column = 2, padx = 50)

        self.entrFileA = Entry(self.master,  bg = 'lightblue')
        self.entrFileA.grid(row = 1, column = 0, columnspan = 2, ipadx = 50)
        self.entrFileB = Entry(self.master,  bg = 'lightblue')
        self.entrFileB.grid(row = 1, column = 2, columnspan = 2, padx = 30, ipadx = 50)

        self.buttonSet = Button(self.master, text='Update', bg='lightgrey', command = lambda: srcFile(self))
        self.buttonSet.grid(row = 2, column = 0, padx = 50)
        self.buttonTransf = Button(self.master, text='Transfer', bg='lightgrey', command = lambda: oper(self))
        self.buttonTransf.grid(row = 2, column = 2, padx = 50)



def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))

    

def file_has_changed(filename):
    #gets file modified time
    file_m_time = datetime.datetime.fromtimestamp(path.getmtime(filename))

    td = datetime.datetime.now() - file_m_time

    if td.days == 0:
        global ready_to_archive
        ready_to_archive = ready_to_archive + 1
        return True
    else: return False


def oper(self):
    global ready_to_archive
    global archive
    ready_to_archive, archived = 0, 0
    
    src_folder = self.entrFileA.get()
    dst_folder = self.entrFileB.get()


    for fname in os.listdir(src_folder):
        src_fname = src_folder + '\%s' % fname

        if file_has_changed(src_fname):
            dst_fname = dst_folder + '\%s' % fname

            try:
                shutil.move(src_fname, dst_folder)
                
                arcived = archived + 1
            except IOError as e:
                print('could not open the file: %s' % e)


if __name__ == '__main__':

    root = tk.Tk()
    App = WindowMain(root)
    root.mainloop
