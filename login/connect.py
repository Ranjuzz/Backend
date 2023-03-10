print("Welcome to the page")
import mysql.connector 
import cgi
form=cgi.FieldStorage()
uid=form.getvalue("username")
pwd=form.getvalue("password")
con = mysql.connector.connect(user='babs' , password='1234' , host='127.0.0.1' , database='project1' )
cur=con.cursor()
cur.execute("insert into login values(uid,pwd)")
con.commit()
cur.close()
con.close()
print(con)
print("<h4>record inserted into the table sucessfully</h4>")