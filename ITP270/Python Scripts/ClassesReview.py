# Defining the Student class and adding a constructor
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        self.grades = grade

# Saving Student instances to variables
roger = Student('Roger van der Weyden', 'year 10')
sandro = Student('Sandro Botticelli', 'year 12')
pieter = Student('Pieter Breugel the Elder', 'year 8')


# Testing the instances
#print(pieter.name)
#print(pieter.year)

#print(sandro.name)
#print(sandro.year)

#print(roger.name)
#print(roger.year)

