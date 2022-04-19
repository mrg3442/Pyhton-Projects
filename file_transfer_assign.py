import shutil
import os
from os import path
import datetime
from datetime import date, time, timedelta

def file_has_changed(fname):
    #gets file modified time
    file_m_time = datetime.datetime.fromtimestamp(path.getmtime(fname))

    td = datetime.datetime.now() - file_m_time

    if td.days == 0:
        global ready_to_archive
        ready_to_archive = ready_to_archive + 1
        return True
    else: return False


def oper():
    global ready_to_archive
    global archive
    ready_to_archive, archived = 0, 0


    for fname in os.listdir('C:\Tech Academy Projects\Python_Projects\Python-Projects\File_transferA'):
        src_fname = 'C:\Tech Academy Projects\Python_Projects\Python-Projects\File_transferA\%s' % fname

        if file_has_changed(src_fname):
            dst_fname = 'C:\Tech Academy Projects\Python_Projects\Python-Projects\File_transferB\%s' % fname
            dst_folder = 'C:\Tech Academy Projects\Python_Projects\Python-Projects\File_transferB'

            try:
                shutil.move(src_fname, dst_folder)
                
                arcived = archived + 1
            except IOError as e:
                print('could not open the file: %s' % e)


if __name__ == '__main__':

    oper()
