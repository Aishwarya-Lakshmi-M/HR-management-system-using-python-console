from connect import cursor,mydb
class Employee:
    def __init__(self, first_name, last_name, date_of_birth, gender, contact_number, email, address, dateofhire,department_id, position_id, salary_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__contact_number = contact_number
        self.__email = email
        self.__address = address
        self.__dateofhire = dateofhire
        self.__department_id = department_id
        self.__position_id = position_id
        self.__salary_id = salary_id
    def get_firstname(self):
        return self.__first_name
    def get_lastname(self):
        return self.__last_name
    def get_date_of_birth(self):
        return self.__date_of_birth
    def get_gender(self):
        return self.__gender
    def get_contact_number(self):
        return self.__contact_number
    def get_email(self):
        return self.__email
    def get_address(self):
        return self.__address
    def get_dateofhire(self):
        return self.__dateofhire
    def get_department_id(self):
        return self.__department_id
    def get_position_id(self):
        return self.__position_id
    def get_salary_id(self):
        return self.__salary_id
class EmployeeDBA:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor
    
    def add_employee(self,employee):
        self.cursor.execute("INSERT INTO employee (firstname, lastname, dateofbirth, gender, contactno, email, address, dateofhire, positionid, salaryid, deptid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (employee.get_firstname(), employee.get_lastname(), employee.get_date_of_birth(), employee.get_gender(), employee.get_contact_number(), employee.get_email(), employee.get_address(),employee.get_dateofhire(), employee.get_department_id(),employee.get_position_id(), employee.get_salary_id()))
        self.cursor.execute("INSERT INTO user (password, role) VALUES(%s,%s)",(str(employee.get_date_of_birth()),"employee"))
        self.mydb.commit()

    def delete_employee(self,emp_id):
        self.cursor.execute("SELECT * FROM employee where idemployee = '%s'",(emp_id,))
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute("DELETE from employee where idemployee = %s",(emp_id,))
            self.mydb.commit()
            return "DELETED"
        return None  
        

    def get_employee(self,emp_id):
        self.cursor.execute("SELECT * FROM employee where idemployee = '%s'",(emp_id,))
        self.mydb.commit()
        result = self.cursor.fetchone()
        if result:
            return result
        return None

    def update_employee_details(self,change, change_value, emp_id):
        self.cursor.execute(f'update employee set  {change} = "%s" where idemployee="%s"' ,(change_value,emp_id,))
        self.mydb.commit()

    def get_employee_details(self):
        self.cursor.execute("SELECT * FROM employee")
        self.mydb.commit()
        result = self.cursor.fetchall()
        if result:return result
        return None
    
    def add_to_projectemp(self,emp_id,project_id):
        self.cursor.execute("INSERT INTO projectemployee VALUES (%s,%s)",(emp_id,project_id))
        self.mydb.commit()

    def calculate_employee_salary(self):
        self.cursor.execute("SELECT firstname,lastname,basesalary - ((basesalary/30)*(select sum(days) from leaveemp where empid = idemployee and status = 'notapproved' )) from employee join salary on employee.salaryid = salary.idsalary")
        result = self.cursor.fetchall()
        return result

class Employeemethods:
    def __init__(self,employee_dba):
        self.employee_dba = employee_dba

    def hire_employee(self,employee):
        self.employee_dba.add_employee(employee)
        print(f"{employee.get_firstname()} {employee.get_lastname()} has been hired.")

    def terminate_employee(self,emp_id):
        result = self.employee_dba.delete_employee(emp_id)
        if result:return "DELETED"
        return "No Such employee existed"


    def view_employee(self,emp_id):
        employee = self.employee_dba.get_employee(emp_id)
        if employee:
            return employee
        return "No such employee"
    
    def view_all_employee(self):
        employee = self.employee_dba.get_employee_details()
        if employee:return employee
        return "No employees hired"
    
    def change_employee_details(self,change,change_value,emp_id):
        self.employee_dba.update_employee_details(change,change_value,emp_id)
        print(f"{change} is modified for employee {emp_id}")

    def assignEmployeeToProject(self,emp_id, project_id):
        self.employee_dba.add_to_projectemp(emp_id,project_id)
        print("assigned")

    def employeesalary(self):
        result = self.employee_dba.calculate_employee_salary()
        return result