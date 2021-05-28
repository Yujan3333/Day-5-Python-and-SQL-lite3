import sqlite3

conn=sqlite3.connect("Students1.sqlite3")
cursor=conn.cursor()

def hash(password):
    return password+"a"

class Students:
    def __init__(self,name,address,rollno,subject):
        self.name=name
        self.address=address
        self.rollno=rollno
        self.subject=subject
    
    def createTable(self):
        # email=""
        # password=""
        # password=hash(password)

        # logininfo=conn.execute(''' Select * from Users where email={email} and password={password}''')
        
        # setsession("user_id")
        
        # user_id=getsession("User_id")

        # user_info=conn.execute(''' Select profile_pic,username,name from users where user_id='user_id''')
        conn.execute('''create table if not exists students
        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Name char(150) NOT NULL,
        Address char(150) NOT NULL,
        Rollno INT NOT NULL,
        Subject char(150) NOT NULL 
        );''')

    def insertData(self):
        self.createTable()
        queryString="insert into students (name,address,rollno,subject) values (?,?,?,?);"
        cursor.execute(queryString,(self.name,self.address,self.rollno,self.subject))
        conn.commit()
        print("Data Inserted Successfully !! ")

    @staticmethod
    def listData():
        queryString="SELECT * from Students"
        results=cursor.execute(queryString)
        print(type(results))
        print("ID\tName\tAddress\tRollno\tSubject")
        for row in results:
            print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(row[4]))

    def update(self,id,newname,newaddress,newroll,newsubject):
        updateSql="UPDATE Students SET name=?,address=?,rollno=?,subject=? WHERE ID=?;"
        cursor=conn.cursor()
        cursor.execute(updateSql,(newname,newaddress,newroll,newsubject,id))
        conn.commit()
        print("Your Data has been Updated Successfully !! ")

    def delete(self,id):
        deleteSql="DELETE FROM Students where ID=?"
        cursor=conn.cursor()
        cursor.execute(deleteSql,(id,))
        conn.commit()
        print("Row Deleted Successfully !! ")
    
    
Std1=Students("Abcd","KTM",15,"Python")
Std1.createTable()  
Std1.insertData()  
Std2=Students("Pravhat","Chakarpath",19,"Time pass ")
Std2.insertData()
print("Before Update")
Students.listData()
print("After Update")
pravat=Students("Abcd","ashdvash",632,"aksdbasmd")
pravat.update(2,"Nitesh","KTM",18,"CSIT")
print("Before Deleting : ")
Students.listData()
paravat=Students("Asbd","asdnasd",15,"asdas")
paravat.delete(2)
print("After Deleting ")
Students.listData()