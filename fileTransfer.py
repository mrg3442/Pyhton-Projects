import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from os import path
import datetime
from datetime import date, time, timedelta
import shutil



class WindowMain(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        #Window Properties
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('300x250')
        self.master.title('File Transfer')

        #Buttons
        self.fileA = Button(self.master,bg='lightgrey', text='File A', command = lambda: browseDirA())
        self.fileA.grid(row=0,column=0, ipadx=60, ipady=50)

        self.fileB = Button(self.master,bg='lightgrey', text='File B', command = lambda: browseDirB())
        self.fileB.grid(row=0,column=1, ipadx=70, ipady=50)

        self.transferbtn = Button(self.master,bg='lightgrey', text='Transfer', command = lambda: oper(self))
        self.transferbtn.grid(row=1,column=0, ipadx=50, ipady=50)




#sets dir A
def browseDirA():
    global dirA
    dirA = filedialog.askdirectory()
    print(dirA)

    
#sets dir B
def browseDirB():
    global dirB
    dirB = filedialog.askdirectory()
    print(dirB)



def file_has_changed(fname):
    #gets file modified time
    file_m_time = datetime.datetime.fromtimestamp(path.getmtime(fname))

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
    
    src_folder = dirA
    dst_folder = dirB


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
