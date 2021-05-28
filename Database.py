import sqlite3

conn=sqlite3.connect("Students.sqlite3")
cursor=conn.cursor()

class Students:
    def __init__(self,name,rollno,sub):
        self.name=name
        self.rollno=rollno
        self.sub=sub

def createTable(self):
    conn.execute('''creates table if not exists students
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name char(150) NOT NULL,
    rollno INT NOT NULL,
    sub char(150) NOT NULL
    );''')
def insertData(self):
    self.createTable()
    queryString="insert into students (name,rollno,sub) values(?,?,?);"
    cursor.execute(queryString,(self.name,self.rollno,self.sub))
    conn.commit()
    print("Data Inserted")

st=Students("yujan",'12','dbms')
# s.createTable()
