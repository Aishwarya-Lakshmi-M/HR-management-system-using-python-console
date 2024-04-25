from connect import cursor,mydb
class Leave:
    def __init__(self,leave_type, start_date, end_date, reason, empid,status):
        self.__leave_type = leave_type
        self.__start_date = start_date
        self.__end_date = end_date
        self.__reason = reason
        self.__empid = empid
        self.__status = status
    def get_leave_type(self):
        return self.__leave_type
    def get_start_date(self):
        return self.__start_date
    def get_end_date(self):
        return self.__end_date
    def get_reason(self):
        return self.__reason
    def get_empid(self):
        return self.__empid
    def get_status(self):
        return self.__status
class leavedba:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor
    
    def add_leave(self,leaves):
        self.cursor.execute(f"SELECT DATEDIFF('{leaves.get_end_date()}','{leaves.get_start_date()}')")
        days = self.cursor.fetchone()
        self.cursor.execute("INSERT INTO leaveemp (leavetype, startdate, enddate, days, reason, empid, status) VALUES (%s,%s,%s,%s,%s,%s)", (leaves.get_leave_type(),leaves.get_start_date(),leaves.get_end_date(),days[0],leaves.get_reason(),leaves.get_empid(),leaves.get_status()))
        self.mydb.commit()
    
    def leave_details(self,leave_id):
        self.cursor.execute("SELECT * FROM leaveemp WHERE idleave = %s",(leave_id,))
        result = self.cursor.fetchone()
        if result:return result
        return None
    
    def empleave(self,emp_id):
        self.cursor.execute("SELECT * FROM leaveemp WHERE empid = %s",(emp_id,))
        result = self.cursor.fetchall()
        if result:return result
        return None
    
    def leave_for_month(self,month,year):
        self.cursor.execute("SELECT * FROM leaveemp where (select month(startdate)) = '%s' and (select year(startdate)) = '%s'",(month,year,))
        result = self.cursor.fetchall()
        if result: return result
        return None
    
    def leave_for_currentmonth(self):
        self.cursor.execute("select * from leaveemp where (select month(startdate)) = (select month(curdate())) and (select year(startdate)) = (select year(curdate()))")
        result = self.cursor.fetchall()
        if result: return result
        return None
    

class leavemethod:
    def __init__(self,leave_db):
        self.leave_db = leave_db

    def new_leave(self,leave):
        self.leave_db.add_leave(leave)
        print(f"added")

    def getLeaveDetails(self,leave_id):
        result = self.leave_db.leave_details(leave_id)
        if result:return result
        return "No such leave"
    
    def getEmployeeLeaveHistory(self,emp_id):
        result = self.leave_db.empleave(emp_id)
        if result:return result
        return "No leave taken still now"
    
    def getleavesofaMonth(self,month,year):
        result = self.leave_db.leave_for_month(month,year)
        if result : return result
        return "No leaves"
    
    def getleavesofCurrentmonth(self):
        result = self.leave_db.leave_for_currentmonth()
        if result : return result
        return "No leaves"


    
