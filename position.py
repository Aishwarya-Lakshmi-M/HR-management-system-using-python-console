from connect import cursor,mydb
class position:
    def __init__(self,position_name, requirements):
        self.__position_name = position_name
        self.__requirements = requirements

    def get_position_name(self):
        return self.__position_name
    def get_requirements(self):
        return self.__requirements

class positiondba:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def add_position(self,position):
        self.cursor.execute("INSERT INTO position (positiontitle,requirements) VALUES (%s,%s)", (position.get_position_name(),position.get_requirements()))
        self.mydb.commit()
        

    def delete_position(self,pos_id):
        self.cursor.execute("SELECT * FROM position WHERE idposition='%s'" %(pos_id,))
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute("DELETE FROM position WHERE idposition='%s'" %(pos_id,))
            return "Deleted successfully"
        return None
    
    def view_position(self,pos_id):
        self.cursor.execute("SELECT * FROM position WHERE idposition='%s'" %(pos_id,))
        result = self.cursor.fetchone()
        if result:
            return result
        return None
    
    def all_position(self):
        self.cursor.execute("SELECT * FROM position")
        result = self.cursor.fetchall()
        if result:return result
        return None

    def retrive_emp(self,pos_id):
        self.cursor.execute("SELECT * FROM employee where positionid = '%s'",(pos_id,))
        result = self.cursor.fetchall()
        if result:return result
        return None

        
    
class positionmethods:
    def __init__(self,position_db):
        self.position_db = position_db
    
    def new_position(self,position):
        self.position_db.add_position(position)
        print(f"{position.get_position_name()} has been added.")

    def remove_position(self,pos_id):
        result = self.position_db.delete_position(pos_id)
        if result:
            return "Deleted successfully"
        return "No such department was added"
    
    def getPositionDetails(self,pos_id):
        result = self.position_db.view_position(pos_id)
        if result:return result
        return None
    
    def getPositionList(self):
        result = self.position_db.all_position()
        if result:return result
        return "No positions exist"
    
    def getEmployeesInPosition(self,pos_id):
        result = self.position_db.retrive_emp(pos_id)
        if result:return result
        return None
    
    