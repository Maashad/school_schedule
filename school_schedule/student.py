""" Initiate class Student """

class Student:
    """ Initiate class Student to hold name, grade, and classes list. """
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, new_class):
        """ Add a new class to classes list. """
        self.classes.append(new_class)
        return self

    def get_num_classes(self):
        """ Return the number of classes for each instance of class Student. """
        return len(self.classes)

    def summary(self):
        """ Return a summary of each Student instance: name, grade, 
        number of classes, and class list """
        print(f'{self.name} is a {self.grade}. {self.name} takes {self.get_num_classes()} classes: {", ".join(self.classes)}')
