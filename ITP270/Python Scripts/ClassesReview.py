# Defining the Student class and adding a constructor
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) == type(Grade):
            self.grades.append(grade)
        elif type(grade) != type(Grade):
            pass
class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


# Saving Student instances to variables
roger = Student('Roger van der Weyden', 'year 10')
sandro = Student('Sandro Botticelli', 'year 12')
pieter = Student('Pieter Breugel the Elder', 'year 8')

pieter_grade = Grade(100)
pieter.grades = pieter.add_grade(pieter_grade)
print(pieter.grades)
# Testing the instances
#print(pieter.name)
#print(pieter.year)

#print(sandro.name)
#print(sandro.year)

#print(roger.name)
#print(roger.year)
