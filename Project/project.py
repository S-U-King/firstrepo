class School:
    pass

class Student(School):
    pass

class Teacher(School):
    pass

class Admin(School):
    pass

class Classrooms(School):
    def __init__(self, class_id, class_name, class_time):
        self.class_id = class_id
        self.class_name = class_name
        self. class_time = class_time

    def getClassrooms(self):    
        return f"id = {self.class_id}, name = {self.class_name}, time = {self.class_time}"
