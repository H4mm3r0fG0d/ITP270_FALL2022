class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}.".format(self.id))

class User:
    def __init__(self, username, role="Customer"):
        self.username = username
        self.role = role

    def say_user_info(self):
        print("My username is {}".format(self.username))
    
    def say_user_role(self):
        print("My role is {}".format(self.role))
    
class Admin(Employee, User):
    # Overriding the say_id method from the Employee class
    def __init__(self):
        super().__init__()
        User.__init__(self, self.id, "Admin")

class Manager(Admin):
    def say_id(self):
        Employee.say_id(self)
        super().say_id()
        print("Manager is in charge")

#e1 = Employee()
#e2 = Employee()
#e3 = Admin()
#e4 = Manager()

#e1.say_id()
#e2.say_id()
#e3.say_id()
#e4.say_user_role()

class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        print("ID {} added.".format(employee.id))
        self.attendees.append(employee)
    
    def add_to_meeting(self, employee):
        self.attendees.append(employee)

    def __len__(self):
        return len(self.attendees)

e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()

m1.add_to_meeting(e1)
m1.add_to_meeting(e2)
m1.add_to_meeting(e3)

print(m1.attendees)
m1 + e1
m1 + e2
m1 + e3

print(len(m1))

