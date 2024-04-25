from connect import cursor,mydb
class Skills:
    def __init__(self,skill_name,description):
        self.__skill_name = skill_name
        self.__description = description
    
    def get_skill_name(self):
        return self.__skill_name
    def get_description(self):
        return self.__description

class skilldba:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def add_skill(self,skill):
        self.cursor.execute("INSERT INTO skills (skillname, skilldescription) VALUES(%s,%s)",(skill.get_skill_name(),skill.get_description()))
        self.mydb.commit()
    
    def delete_skill(self,skill_id):
        self.cursor.execute("SELECT * FROM skills WHERE idskill = '%s'",(skill_id,))
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute("DELETE FROM skills WHERE idskill='%s'" %(skill_id,))
            return "Deleted successfully"
        return None

    def add_to_skillemp(self,emp_id,skill_id):
        self.cursor.execute("INSERT INTO skillsemployee VALUES (%s,%s)",(emp_id,skill_id))
        self.mydb.commit()

    def get_empskills(self,emp_id):
        self.cursor.execute("SELECT * FROM skills WHERE idskill in (SELECT skillid from skillsemployee where empid = '%s')",(emp_id,))
        result = self.cursor.fetchall()
        if result:
            return result
        return None
    
    def get_skill(self,skill_id):
        self.cursor.execute("SELECT * FROM skills WHERE idskill = '%s'",(skill_id,))
        result = self.cursor.fetchone()
        if result:
            return result
        return None
    
    def all_skill(self):
        self.cursor.execute("SELECT * FROM skills")
        result = self.cursor.fetchall()
        if result:return result
        return None



class skillmethods:
    def __init__(self,skill_db):
        self.skill_db = skill_db

    def new_skill(self,skill):
        self.skill_db.add_skill(skill)
        print(f"{skill.get_skill_name()} was added")
    
    def remove_skill(self,skill_id):
        result = self.skill_db.delete_skill(skill_id)
        if result:
            return "Deleted successfully"
        return "No such skill available"
    
    def addSkillToEmployee(self,emp_id,skill_id):
        self.skill_db.add_to_skillemp(emp_id,skill_id)
        print("added")

    def getEmployeeSkills(self,emp_id):
        result = self.skill_db.get_empskills(emp_id)
        if result:
            return result
        return "No skills are added"
    
    def getSkillDetails(self,skill_id):
        result = self.skill_db.get_skill(skill_id)
        if result:
            return result
        return "No such skill available"
    
    def getskilllist(self):
        result = self.skill_db.all_skill()
        if result:return result
        return "No salary exist"