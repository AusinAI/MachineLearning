class Student:
    def __init__(self,name=""):
        self.name = name

obj = Student("Utkarsh")


class Family:
    members = 5
    def __init__(self, count):
        print("This is a Constructor")
        self.members = count
    def show(self):
        print("Number of members is " ,self.members)

object = Family(10)

class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("Id: ",self.id)
        print("Name: ",self.name)

emp1 = Employee("Utkarsh",101)
emp2 = Employee("Ausin",102)

print(emp1.id)
print(emp1.name)


emp1.display()
emp2.display()


