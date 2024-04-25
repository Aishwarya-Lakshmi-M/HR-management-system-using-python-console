import mysql.connector

mydb = mysql.connector.connect(host = "localhost",user = "root",password = "root",database = "hr_management_system")
cursor = mydb.cursor(buffered=True)
