from school_schedule.student import Student
from school_schedule.high_school_student import HighSchoolStudent

#first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

quinn.add_class("Painting")
quinn.get_num_classes()
quinn.summary()

# second instance
claire = HighSchoolStudent(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ],
                True
            )

claire.get_num_classes()
claire.summary()
claire.has_parking_priviliges()

# Extra:
# - create a function that will return the student with more classes
# - create a test for that function