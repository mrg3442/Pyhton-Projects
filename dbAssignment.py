import os
import sqlite3

fPath = os.path.join("C:\Tech Academy Projects\Python_Projects\Python-Projects\dbAssignment")

conn = sqlite3.connect('db_assignment.db')

#Checks fileList for ending in .txt then updates database 
def check_txt():
    for x in fileList:
        if x.endswith('.txt'):
            conn = sqlite3.connect('db_assignment.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_textFiles) VALUES(?)", (fName,))
                conn.commit()
            conn.close()
    


#Prints data currently in tbl_files
def check_table():
    conn = sqlite3.connect('db_assignment.db')
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM tbl_files')
        y = cur.fetchall()
        print("These files end in '.txt'.... \n\n\n {}".format(y))
    conn.close()

# creates table if it does not already exist
def create_tbl(tbl):
    conn = sqlite3.connect('db_assignment.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS {}".format(tbl))
        conn.commit()
    conn.close()


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


if __name__ == '__main__':
    create_tbl('tbl_files( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_textFiles \
                )')
    check_txt()
    check_table()
    
    
