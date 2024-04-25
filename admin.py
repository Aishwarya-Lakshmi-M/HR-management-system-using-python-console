from connect import cursor,mydb
from tabulate import tabulate
from employee import *
from department import *
from leave import *
from project import *
from skill import *
from training import *
from position import *
from salary import *

class Admin:
    def __init__(self,admin_id,password):
        self.__admin_id = admin_id
        self.__password = password
    def get_admin_id(self):
        return self.__admin_id
    def get_password(self):
        return self.__password
    
class admindba:
    def __init__(self):
        self.cursor = cursor
        self.mydb = mydb
    def validation(self,admin):
        self.cursor.execute("SELECT * FROM user WHERE iduser = %s AND password = %s AND role = 'admin'",(admin.get_admin_id(),admin.get_password()))
        result = self.cursor.fetchone()
        if result:return True
        return False
class adminview:
    def __init__(self,admin_dba):
        self.admin_dba = admin_dba
    def access(self,admin):
        result = self.admin_dba.validation(admin)
        if result:
            def mainmenu():
                print("***********Welcome************")
                print("Payroll report - 10")
                print("Access Employee - 1\nAccess Department - 2\nAccess Leave - 3\nAccess Projects - 4\nAccess Skills - 5\nAccess Salary - 6\nAccess Training - 7\nAccess position - 8\nEXIT - 9")
                option = int(input("CHOOSE FROM THE ABOVE OPTIONS: "))
                while option not in (1,2,3,4,5,6,7,8,9,10):
                    option = int(input("CHOOSE THE CORRECT OPTION: "))
                if option == 9:
                    print("THANK YOU!! SEE YOU AGAIN:)")
                elif option == 1:
                    def employeeoptions():
                        print("To Hire Employee - 1\nTo Terminate Employee - 2\nTo View Employee - 3\nEmployee List - 4\nTo assign project - 5\nModify Employee Details - 6\nBACK - 7")
                        option = int(input("CHOOSE FROM THE ABOVE OPTIONS: "))
                        while option not in (1,2,3,4,5,6,7):
                            option = int(input("CHOOSE THE CORRECT OPTION: "))
                        employee_db = EmployeeDBA()
                        employee_meth = Employeemethods(employee_db)
                        if option == 1:
                            employee = Employee(first_name = input("Enter the first name: "), last_name = input("Enter the last name: "), date_of_birth = input("Enter the Date of birth: "), gender=input("Enter the gender: "), contact_number= input("Enter the contact no: "), email = input("Enter the email: "), address = input("Enter the house address: "), dateofhire = input("Enter the Date of hire: "),department_id = int(input("Enter the positionid: ")), position_id = int(input("Enter the salaryid: ")), salary_id = int(input("Enter the departmentid: ")))
                            employee_meth.hire_employee(employee)
                        elif option == 2:
                            empid = int(input("Enter the employee ID: "))
                            print(employee_meth.terminate_employee(empid))
                        elif option==3:
                            t = ("Employee Id: ","first_name: ", "last_name: ", "date_of_birth: ", "gender: ", "contact_number: ", "email: ", "address: ", "dateofhire: ","department_id: ", "position_id: ", "salary_id: ")
                            empid = int(input("Enter the employee ID: "))
                            result = employee_meth.view_employee(empid)
                            for i in range(len(result)):
                                print(t[i],result[i])
                        elif option==4:
                            t = ("Employee Id","first_name", "last_name", "date_of_birth", "gender", "contact_number", "email", "address", "dateofhire","department_id", "position_id", "salary_id")
                            result = employee_meth.view_all_employee()
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option==5:
                            emp_id,project_id = int(input("Enter the Employee ID: ")),int(input("Enter the project ID: "))
                            employee_meth.assignEmployeeToProject(emp_id, project_id)
                        elif option==6:
                            empid = int(input("Enter the employee id: "))
                            modifykey = {1: "contactno",2 : "email", 3:"address",4:"deptid",5:"positionid",6:"salaryid"}
                            print("Contact number: 1\nEmail Address: 2\nAddress: 3\nDepartment ID: 4\nPosition Id: 5\nSalary Id: 6")
                            tomodify = int(input("Choose from above options: "))
                            if tomodify in (1,2,3):
                                change = input(f"Enter the updated {modifykey[tomodify]}: ")
                            else:change = int(input(f"Enter the updated {modifykey[tomodify]}: "))
                            employee_meth.change_employee_details(modifykey[tomodify],change,empid)
                        elif option==7:
                            mainmenu()
                            return
                        print("*"*100)
                        employeeoptions()
                    employeeoptions()

                elif option==2:
                    def departmentoptions():
                        print("To add new Department - 1\nTo Delete Department - 2\nTo View Department Details - 3\nDepartment List - 4\nBACK - 5")
                        option = int(input("CHOOSE FROM THE ABOVE OPTIONS: "))
                        while option not in (1,2,3,4,5):
                            option = int(input("CHOOSE THE CORRECT OPTION: "))
                        department_db = departmentDBA()
                        department_service = Departmentmethods(department_db)
                        if option == 1:
                            dept = department(dept_name=input("Enter the department name: "))
                            department_service.new_department(dept)
                        elif option == 2:
                            try:
                                print(department_service.remove_department(int(input("Enter the deptid: "))))
                            except:
                                print("The department cannot be deleted as employees are still assigned to this department")
                        elif option == 3:
                            tab = ["Department ID: ","Department Name: "]
                            result = (department_service.getDepartmentDetails(int(input("Enter the Department Id: "))))
                            for i in range(len(tab)):print(tab[i],result[i])
                        elif option == 4:
                            t = ("Department ID: ","Department Name: ")
                            result = department_service.getDepartmentList()
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option == 5:
                            mainmenu()
                            return
                        print("*"*100)
                        departmentoptions()
                    departmentoptions()

                elif option == 3:
                    def leaveoptions():
                        print("New Leave - 1\nGet leave details - 2\nTo View Employee leave history - 3\nView Leaves of a month - 4\nleaves of the current month - 5\nBACK - 6")
                        option = int(input("CHOOSE FROM THE ABOVE OPTIONS: "))
                        while option not in (1,2,3,4,5,6):
                            option = int(input("CHOOSE THE CORRECT OPTION: "))
                        leave_db = leavedba()
                        leave_service = leavemethod(leave_db)
                        if option == 1:
                            leave = Leave(leave_type=input("Enter the leave type: "), start_date = input("Start date: "), end_date = input("End date: "), reason = input("Enter the reason: "), empid = int(input("Enter the Employee ID: ")))
                            leave_service.new_leave(leave)
                        elif option == 2:
                            t = ("Leave Id:","Leave type:","Start date:","End date:","Total Days:","Reason:","Employee ID:")
                            result = (leave_service.getLeaveDetails(int(input("Enter the leave ID: "))))
                            for i in range(len(t)):print(t[i],result[i])
                        elif option == 3:
                            t = ("Leave Id","Leave type","Start date","End date","Total Days","Reason","Employee ID")
                            result = leave_service.getEmployeeLeaveHistory(int(input("Enter the Employee ID: ")))
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option == 4:
                            print("January: 1\nFeb: 2\nMarch: 3\nApril: 4\nMay: 5\nJune: 6\nJuly: 7\nAugust: 8\nSept: 9\nOct: 10\nNovember: 11\nDecember: 12")
                            month = int(input("CHOOSE THE MONTH: "))
                            year = int(input("Enter the year: "))
                            t = ("Leave Id","Leave type","Start date","End date","Total Days","Reason","Employee ID")
                            result = (leave_service.getleavesofaMonth(month,year))
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option == 5:
                            t = ("Leave Id","Leave type","Start date","End date","Total Days","Reason","Employee ID")
                            result = leave_service.getleavesofCurrentmonth()
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option == 6:
                            mainmenu()
                            return
                        print("*"*100)
                        leaveoptions()
                    leaveoptions()
                elif option == 4:
                    def projectoptions():
                        project_db = projectdba()
                        project_service = projectmethods(project_db)
                        print("New Project - 1\nget current month projects- 2\nAdd Employee to Project - 3\nView projects of a employee - 4\nView all projects - 5\nView project details - 6\nRemove project - 7\nBACK - 8")
                        option = int(input("CHOOSE FROM THE ABOVE OPTIONS: "))
                        while option not in (1,2,3,4,5,6,7,8):
                            option = int(input("CHOOSE THE CORRECT OPTION: "))
                        if option == 1:
                            newproject = Project(projecttitle=input("Enter the project title: "),description=input("Description: "),start_date=input("Enter the starting date: "),end_date=input("Enter the ending date: "),empmanagerid=int(input("Enter the project manager id: ")))
                            project_service.new_project(newproject)
                        elif option == 7:
                            print(project_service.cancel_project(int(input("Enter the project Id: "))))
                        elif option == 5:
                            t = ("Project Id","Project Title","Description","Start Date","End Date","Project manager Id")
                            result = project_service.getprojectlist()
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option == 3:
                            project_service.addProjectToEmployee(int(input("Enter the employee Id: ")),int(input("Enter the project Id: ")))
                            
                        elif option == 4:
                            t = ("Project Id","Project Title","Description","Start Date","End Date","Project manager Id")
                            result = project_service.getEmployeeProjects(int(input("Enter the employee Id: ")))
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option == 2:
                            t = ("Project Id","Project Title","Description","Start Date","End Date","Project manager Id")
                            result = project_service.getcurrentprojects()
                            if result == None:print("No project Exists")
                            else:
                                tab = ()
                                tab=(*tab,t)
                                for i in result:tab=(*tab,i)
                                print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option==6:
                            t = ("Project Id:","Project Title:","Description:","Start Date:","End Date:","Project manager Id:")
                            result = project_service.getProjectDetails(int(input("Enter the project Id: ")))
                            for i in range(len(t)):print(t[i],result[i])
                        elif option==8:
                            mainmenu()
                            return
                        print("*"*100)
                        projectoptions()
                    projectoptions()
                elif option == 5:
                    def skilloptions():
                        skill_db = skilldba()
                        skill_service = skillmethods(skill_db)
                        print("New skill - 1\nRemove skill- 2\nAdd skill to Employee- 3\nGet employee skills - 4\nGet skill details- 5\nView skill list- 6\nBACK - 7")
                        option = int(input("CHOOSE FROM THE ABOVE OPTIONS: "))
                        while option not in (1,2,3,4,5,6,7):
                            option = int(input("CHOOSE THE CORRECT OPTION: "))
                        if option==1:
                            newskill = Skills(skill_name=input("Enter the skill name: "),description=input("Enter the skill description: "))
                            skill_service.new_skill(newskill)
                        elif option == 2:
                            try: 
                                print(skill_service.remove_skill(int(input("Enter the skill id: "))))
                            except:
                                print("Employees still have these skill, unable to remove skill details")
                        elif option == 3:
                            skill_service.addSkillToEmployee(int(input("Enter the Employee Id: ")),int(input("Enter the Skill Id: ")))
                        elif option == 4:
                            t = ("skill ID","skill name","Description")
                            result = skill_service.getEmployeeSkills(int(input("Enter the employee ID: ")))
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option == 5:
                            t = ("skill ID:","skill name:","Description:")
                            result = skill_service.getSkillDetails("Enter the skill id: ")
                            for i in range(len(t)):print(t[i],result[i])
                        elif option == 6:
                            t = ("skill ID","skill name","Description")
                            result = skill_service.getskilllist()
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option==7:
                                mainmenu()
                                return
                        print("*"*100)
                        skilloptions()
                    skilloptions()
                elif option == 6:
                    def salaryoption():
                        salary_db = salarydba()
                        salaryservice = salarymethods(salary_db)
                        print("New salary - 1\nRemove salary- 2\nGet Employee salary- 3\nView salary details - 4\nView all salary - 5\nBACK - 6")
                        option = int(input("CHOOSE FROM THE ABOVE OPTIONS: "))
                        while option not in (1,2,3,4,5,6,):
                            option = int(input("CHOOSE THE CORRECT OPTION: "))
                        if option == 1:
                            newsalary = Salary(float(input("Enter the base salary")),float(input("Enter the pf amount: ")))
                            salaryservice.new_salary(newsalary)
                        elif option == 2:
                            print(salaryservice.remove_salary(int(input("Enter the employee ID: "))))
                        elif option == 3:
                            t = ("Salary ID: ","Base amount: ","PF: ")
                            result = salaryservice.getEmployeeSalary(int(input("Enter the employee ID: ")))
                            if result:
                                for i in range(len(t)):print(t[i],result[i])
                            else:print("No such employee exist")
                        elif option == 4:
                            t = ("Salary ID: ","Base amount: ","PF: ")
                            result = salaryservice.getSalaryDetails(int(input("Enter the salary ID: ")))
                            if result:
                                    for i in range(len(t)):print(t[i],result[i])
                            else:print("No such salary exists")
                        elif option == 5:
                            t = ("Salary ID","Base amount","PF")
                            result = salaryservice.getsalarylist()
                            if result:
                                tab = ()
                                tab=(*tab,t)
                                for i in result:tab=(*tab,i)
                                print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                            else:print("Salary list is yet not filled")
                                
                        elif option==6:
                                mainmenu()
                                return
                        print("*"*100)
                        salaryoption()
                    salaryoption()
                elif option == 7:
                    def trainingoptions():
                        training_db = trainingdba()
                        training_service = trainingmethods(training_db)
                        print("To schedule training - 1\nTo cancel training- 2\nTo update training schedule- 3\nTo mark complete training - 4\nTo view scheduled training- 5\nTo view completed training- 6\nTo register employee for training - 7\nTo withdraw employee from training - 8\nGet participants - 9\nView all trainings - 10\nBACK - 11")
                        option = int(input("CHOOSE FROM THE ABOVE OPTIONS: "))
                        while option not in (1,2,3,4,5,6,7,8,9,10,11,):
                            option = int(input("CHOOSE THE CORRECT OPTION: "))
                        if option==1:
                            new_taining = Training(input("Enter the training title: "),input("Enter description: "),input("Enter the starting date: "),input("Enter the ending date: "),input("Enter the traininer name: "),"scheduled")
                            training_service.schedule_training(new_taining)
                        elif option == 2:
                            print(training_service.cancel_training(int(input("Enter the training ID: "))))
                        elif option == 3:
                            modifykey = {1: "startdate",2 : "enddate"}
                            print("Starting date: 1\nEnding date: 2")
                            tomodify = int(input("Choose from above options: "))
                            training_service.updateTrainingSchedule(modifykey[tomodify],int(input("Enter the training ID: ")),input("Enter the new date: "))
                        elif option == 4:
                            training_service.completeTraining(int(input("Enter the training ID: ")))
                        elif option==5:
                            t = ("Training Id","Training title","Description","Starting Date","Ending Date","Trainer","Status")
                            result = training_service.getScheduledTrainings()
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option==6:
                            t = ("Training Id","Training title","Description","Starting Date","Ending Date","Trainer","Status")
                            result = training_service.getCompletedTrainings()
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                            
                        elif option==7:
                            training_service.registerEmployeeForTraining(int(input("Enter the employee ID: ")),int(input("Enter the training ID: ")))
                        elif option==8:
                            training_service.withdrawEmployeeFromTraining(int(input("Enter the employee ID: ")),int(input("Enter the training ID: ")))
                        elif option==9:
                            result = training_service.getParticipants(int(input("Enter the training ID: ")))
                            t = ("Employee Id","first_name", "last_name", "date_of_birth", "gender", "contact_number", "email", "address", "dateofhire","department_id", "position_id", "salary_id")
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option== 10:
                            result = training_service.viewalltrainings()
                            t = ("Training Id","Training title","Description","Starting Date","Ending Date","Trainer","Status")
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option==11:
                                mainmenu()
                                return
                        print("*"*100)
                        trainingoptions()
                    trainingoptions()
                elif option == 8:
                    def positionoptions():
                        position_db = positiondba()
                        position_service = positionmethods(position_db)
                        print("To add new position - 1\nTo remove position - 2\nview position details - 3\nView all positions - 4\nGet employees - 5\nBACK - 6")
                        option = int(input("CHOOSE FROM THE ABOVE OPTIONS: "))
                        while option not in (1,2,3,4,5,6):
                            option = int(input("CHOOSE THE CORRECT OPTION: "))
                        if option==1:
                            newposition = position(input("Enter the position name: "),input("Enter the position requirements: "))
                            position_service.new_position(newposition)
                        elif option == 2:
                            try:
                                print(position_service.remove_position(int(input("Enter the position Id: "))))
                            except:print("This position is assigned to an employee")
                        elif option == 3:
                            t = ("position ID:","Position name:","Requirements:")
                            result = (position_service.getPositionDetails(int(input("Enter the position ID: "))))
                            if result:
                                for i in range(len(t)):print(t[i],result[i])
                            else:print("No such position exist")
                        elif option == 4:
                            result = position_service.getPositionList()
                            t = ("position ID","Position name","Requirements")
                            tab = ()
                            tab=(*tab,t)
                            for i in result:tab=(*tab,i)
                            print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                        elif option == 5:
                            result = position_service.getEmployeesInPosition(int(input("Enter the position ID: ")))
                            if result:
                                t = ("Employee Id","first_name", "last_name", "date_of_birth", "gender", "contact_number", "email", "address", "dateofhire","department_id", "position_id", "salary_id")
                                tab = ()
                                tab=(*tab,t)
                                for i in result:tab=(*tab,i)
                                print(tabulate(tab,headers='firstrow',tablefmt='fancy_grid'))
                            else:print("No employee exist")
                        elif option==6:
                                mainmenu()
                                return
                        print("*"*100)
                        positionoptions()
                    positionoptions()
                elif option == 10:
                    employee_db = EmployeeDBA()
                    employee_meth = Employeemethods(employee_db)
                    result = employee_meth.employeesalary()
                    print(result)
            mainmenu()
            





                
                    

                    










        else:
            print("USERID OR PASSWORD IS Incorrect")
            aobj = Admin(int(input("Enter The userid: ")),input("Enter the password: "))
            admin_db = admindba()
            adminviews = adminview(admin_db)
            adminviews.access(aobj)

aobj = Admin(int(input("Enter The userid: ")),input("Enter the password: "))
admin_db = admindba()
adminviews = adminview(admin_db)
adminviews.access(aobj)

