# Creating the School class
class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = int(numberOfStudents)

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def set_numberOfStudents(self, new_number):
        self.numberOfStudents = new_number

    def get_numberOfStudents(self):
        return self.numberOfStudents
        
    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."

# Creating the Primary School class
class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "Primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.pickupPolicy
    
    def __repr__(self):
        return super().__repr__() + " " + f"Also, the pickup policy is {self.pickupPolicy}"

# Creating the High School class
class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "High", numberOfStudents)
        self.sportsTeams = []
        self.sportsTeams.append(sportsTeams)

    def get_sportsTeams(self):
        return sportsTeams

    def set_sportsTeams(self, sportsTeams):
        self.sportsTeams.append(sportsTeams)

    def __repr__(self):
        return super().__repr__() + " " + f"And the sports teams are the {self.sportsTeams[0]}"

#stleo_elementary = School("St. Leo The Great Catholic School", "Primary", 350)
#print(stleo_elementary)
#print(stleo_elementary.get_name())
#print(stleo_elementary.get_level())
#print(stleo_elementary.get_numberOfStudents())

#stleo_elementary.set_numberOfStudents(250)
#print(stleo_elementary.get_numberOfStudents())

# Creating an instance of the Primary School class and printing for verification
ps1 = PrimarySchool("Saint Leo the Great Catholic School", 350, "parent pickup/dropoff")

print(ps1)

# Creating an instance of the High School class and printing for verification
hs1 = HighSchool("James W. Robinson Secondary", 5000, "Rams")

print(hs1)