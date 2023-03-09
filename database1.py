import sqlite3



#creating database test1
conn = sqlite3.connect('test1.db')

#creating a tbl_location if it does not exist
#There is a auto increment primary integer column and a Text column for string types
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_location( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_file)")
    conn.commit()
conn.close

conn = sqlite3.connect('test1.db')

#created a string of files with different types
fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg',\
            'World.txt','data.pdf','myPhoto.jpg')

# for loop will iterate filList for files that end in txt and add it to col_file column in database
#it will end by printing the txt files to Python
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_location (col_file) VALUES (?)", \
                        (x,))
            print(x)
            conn.commit
conn.close
