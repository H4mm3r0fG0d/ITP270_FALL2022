#class Employee():
#    def __init__(self):
#        self.id = None
#        self._id = "S"
#        self.__id = "I"

#e = Employee()

class Employee():
    new_id = 1
    def __init__(self, name=None):
        self.id = Employee.new_id
        Employee.new_id += 1
        