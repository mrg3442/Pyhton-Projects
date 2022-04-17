import sqlite3
import re


conn = sqlite3.connect('db_assignment.db')
fileList  = ('information.docx', 'Hello.txt', 'myImage.png', \
             'myMovie.mpg', 'World.txt','data.pdf', 'myPhoto.jpg')

def create_database():
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_textFiles TEXT \
                    )")
        conn.commit()
def find_txt():
    for i in fileList:
        var1 = fileList.endswith('.txt,')
        print(fileList)
        




if __name__ == '__main__':
    find_txt()
    
