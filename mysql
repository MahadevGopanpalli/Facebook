import mysql.connector

cnx = mysql.connector.connect(user='Vaibhav', password='vk18',
                              host='localhost',
                              database='python')

if (cnx):
    print ("Connected")
else:
    print ("Not COnnected")
    
mycursor = cnx.cursor()

mycursor.execute("SELECT T1.* FROM T1 LEFT JOIN T2 ON (T1.id = T2.id) WHERE T2.id IS NULL")
R1 = mycursor.fetchall()

mycursor.execute("SELECT T2.* FROM T2 LEFT JOIN T1 ON (T1.id = T2.id) WHERE T1.id IS NULL")
R2= mycursor.fetchall()

for i in R1:
    i=list(i)
    mycursor.execute("Insert into  T3 values({})".format(int(i[0])))
for i in R2:
    i=list(i)
    mycursor.execute("Insert into  T3 values({})".format(int(i[0])))

mycursor.execute("SELECT * from T3")
Result= mycursor.fetchall()

for i in Result:
    print (i)
    
cnx.close()
