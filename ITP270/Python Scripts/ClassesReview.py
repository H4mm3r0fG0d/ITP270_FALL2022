# Defining the Student class and adding a constructor
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
# Defining the add grade function
    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade.score)

# Creating and defining the Grade class
class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

# Saving Student instances to variables
roger = Student('Roger van der Weyden', 'year 10')
sandro = Student('Sandro Botticelli', 'year 12')
pieter = Student('Pieter Breugel the Elder', 'year 8')

# Adding a new grade with score of 100 to Pieter's grade attribute
pieter.add_grade(Grade(100))

# Testing the instances
#print(pieter.name)
#print(pieter.year)
#print(pieter.grades)

#print(sandro.name)
#print(sandro.year)

#print(roger.name)
#print(roger.year)

