from connect import cursor,mydb
class Salary:
    def __init__(self,basesalary,pf):
        self.__basesalary = basesalary
        self.__pf = pf
    def get_base_salary(self):
        return self.__basesalary
    def get_pf(self):
        return self.__pf

class salarydba:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def add_salary(self,salary):
        self.cursor.execute("INSERT INTO salary (idsalary, basesalary, bonus) VALUES (%s,%s)",(salary.get_base_salary(),salary.get_pf()))
        self.mydb.commit()
        print(f"{salary.salary_id} has been added")

    def delete_salary(self,salary_id):
        self.cursor.execute("SELECT * FROM salary WHERE idsalary = '%s'",(salary_id,))
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute("DELETE FROM salary WHERE idsalary='%s'" %(salary_id,))
            return "Deleted successfully"
        return None
    
    def get_empsalary(self,emp_id):
        self.cursor.execute("SELECT * FROM salary WHERE idsalary = (SELECT salaryid from employee where idemployee = '%s')",(emp_id,))
        result = self.cursor.fetchone()
        if result:
            return result
        return None
    
    def get_salary(self,salary_id):
        self.cursor.execute("SELECT * FROM salary WHERE idsalary = '%s'",(salary_id,))
        result = self.cursor.fetchone()
        if result:
                return result
        return None
    
    def all_salary(self):
        self.cursor.execute("SELECT * FROM salary")
        result = self.cursor.fetchall()
        if result:return result
        return None



class salarymethods:
    def __init__(self,salary_db):
        self.salary_db = salary_db 
    def new_salary(self,salary):
        self.salary_db.add_salary(salary)
        print("New salary package added")

    def remove_salary(self,salary_id):
        result = self.salary_db.delete_salary(salary_id)
        if result:
            return "Deleted successfully"
        return "No such salary package"
    
    def getEmployeeSalary(self,emp_id):
        result = self.salary_db.get_empsalary(emp_id)
        if result:
            return result
        return "No employee gets this salary"
    
    def getSalaryDetails(self,salary_id):
        result = self.salary_db.get_salary(salary_id)
        if result:
            return result
        return "No such salary package"
    
    def getsalarylist(self):
        result = self.salary_db.all_salary()
        if result:return result
        return "No salary exist"