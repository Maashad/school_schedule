""" Initiate class high school student """
from .student import Student

class HighSchoolStudent(Student):
    """ define class HighSchoolStudent """
    def __init__(self,
                name,
                grade,
                classes,
                has_parking_priviliges=False):
        super().__init__(name, grade, classes)
        # self.has_parking_privileges
    