from connect import cursor,mydb
class Training:
    def __init__(self,training_title,description,start_date,end_date,trainer,status):
        self.__training_title = training_title
        self.__description = description
        self.__start_date = start_date
        self.__end_date = end_date
        self.__trainer = trainer
        self.__status = status
    
    def get_training_title(self):
        return self.__training_title
    def get_description(self):
        return self.__description
    def get_start_date(self):
        return self.__start_date
    def get_end_date(self):
        return self.__end_date
    def get_trainer(self):
        return self.__trainer
    def get_status(self):
        return self.__status

class trainingdba:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def add_training(self,training):
        self.cursor.execute("INSERT INTO training (trainingtitle, description, startdate, enddate, trainer, status) VALUES(%s,%s,%s,%s,%s,%s)",(training.get_training_title(),training.get_description(),training.get_start_date(),training.get_end_date(),training.get_trainer(),training.get_status()))
        self.mydb.commit()

    def delete_training(self,training_id):
        self.cursor.execute("SELECT * FROM training WHERE idtraining = '%s'",(training_id,))
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute("delete from trainingemployee where trainingid = %s",(training_id,))
            self.mydb.commit()
            self.cursor.execute("DELETE FROM training WHERE idtraining ='%s'" %(training_id,))
            self.mydb.commit()
            return "Deleted successfully"
        return None
    
    def modify_time(self, change, training_id, new_date):
        self.cursor.execute("SELECT * FROM training WHERE idtraining = '%s'",(training_id,))
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute(f'update training set  {change} = {new_date} where idtraining = {training_id}')
            self.mydb.commit()
            return "updated"
        return None

    def modify_status(self,training_id):
        self.cursor.execute("SELECT * FROM training WHERE idtraining = '%s'",(training_id,))
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute('update training set status = "completed" where idtraining=%s' ,(training_id,))
            self.mydb.commit()
            return "updated"
        return None
    
    def trainings_between_dates(self):
        self.cursor.execute('SELECT * FROM training WHERE  status = "scheduled"')
        result = self.cursor.fetchall()
        if result:return result
        return None
    
    def complete_training(self):
        self.cursor.execute('SELECT * FROM training where status = "completed"')
        result = self.cursor.fetchall()
        if result:return result
        return None
    
    def add_employeeTotraining(self,emp_id,training_id):
        self.cursor.execute("SELECT * FROM trainingemployee WHERE trainingid = '%s' and empid = '%s'",(training_id,emp_id,))
        result = self.cursor.fetchone()
        if result:
            return "Already exist"
        else:
            self.cursor.execute("INSERT INTO trainingemployee VALUES(%s,%s)",(emp_id,training_id))
            self.mydb.commit()
            return None

    def delete_employeeTotraining(self,emp_id,training_id):
        self.cursor.execute("SELECT * FROM trainingemployee WHERE trainingid = %s and empid = %s",(emp_id,training_id,))
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute("DELETE FROM trainingemployee WHERE trainingid = %s and empid = %s",(emp_id,training_id,))
            return "Deleted successfully"
        return None
    
    def all_trainingemp(self,training_id):
        self.cursor.execute("SELECT * FROM employee where idemployee in (select empid from trainingemployee WHERE trainingid = %s)",(training_id,))
        result = self.cursor.fetchall()
        if result:return result
        return None
    def all_training(self):
        self.cursor.execute("select * from training")
        result = self.cursor.fetchall()
        if result:return result
        return None


class trainingmethods:
    def __init__(self,training_db):
        self.training_db = training_db

    def schedule_training(self,training):
        self.training_db.add_training(training)
        print(f"{training.get_training_title()} is scheduled")

    def cancel_training(self,training_id):
        result = self.training_db.delete_training(training_id)
        if result:
            return "cancelled successfully"
        return "No such training scheduled"
    
    def updateTrainingSchedule(self, change, training_id, new_date):
        result = self.training_db.modify_time(change, training_id, new_date)
        if result:print("modified")
        else:print("No such training exist")
    
    def completeTraining(self,training_id):
        result = self.training_db.modify_status(training_id)
        if result:print(f"{training_id} training completed")
        else:print("No such training exist")

    def getScheduledTrainings(self):
        result = self.training_db.trainings_between_dates()
        if result:return result
        return "No training scheduled"
    
    def getCompletedTrainings(self):
        result = self.training_db.complete_training()
        if result:return result
        return "No completed trainings"
    
    def registerEmployeeForTraining(self,emp_id, training_id):
        result = self.training_db.add_employeeTotraining(emp_id,training_id)
        if result: print("already Registered")
        else: print("registered")

    def withdrawEmployeeFromTraining(self,emp_id, training_id):
        result = self.training_db.delete_employeeTotraining(emp_id,training_id)
        if result: print("Withdrawn")
        else: print("No such employee eas registered")

    def getParticipants(self,training_id):
        result = self.training_db.all_trainingemp(training_id)
        if result:return result
        return "No participants registered"
    def viewalltrainings(self):
        result = self.training_db.all_training()
        if result:return result
        return "No training scheduled"
