from connect import cursor,mydb
class department:

    def __init__(self,dept_name):
        self.__dept_name = dept_name

    def get_dept_name(self):
        return self.__dept_name
    
class departmentDBA:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def add_department(self,department):
        self.cursor.execute("INSERT INTO department (deptname) VALUES (%s)", (department.get_dept_name(),))
        self.mydb.commit()

    def delete_department(self,dept_id):
        self.cursor.execute("SELECT * FROM department WHERE iddepartment='%s'" %(dept_id,))
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute("DELETE FROM department WHERE iddepartment='%s'" %(dept_id,))
            self.mydb.commit()
            return "Deleted successfully"
        return None
    
    def view_department(self,dept_id):
        self.cursor.execute("SELECT * FROM department WHERE iddepartment='%s'" %(dept_id,))
        result = self.cursor.fetchone()
        if result:
            return result
        return None
    
    def all_department(self):
        self.cursor.execute("SELECT * FROM department")
        result = self.cursor.fetchall()
        if result:return result
        return None
        

class Departmentmethods:
    def __init__(self,department_dba):
        self.department_dba = department_dba
    
    def new_department(self,department):
        self.department_dba.add_department(department,)
        print(f"{department.get_dept_name()} has been added.")

    def remove_department(self,dept_id):
        result = self.department_dba.delete_department(dept_id)
        if result:
            return "Deleted successfully"
        return "No such department"
    
    def getDepartmentDetails(self,dept_ID):
        result = self.department_dba.view_department(dept_ID)
        if result:return result
        return "No such department exist"
    
    def getDepartmentList(self):
        result = self.department_dba.all_department()
        if result:return result
        return "No departments exist"