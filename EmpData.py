class Employee:
    def __init__(self, name, empID):
        self.name = name
        self.empID = empID
        self.salary= None
    def calcSalary(self):
        raise NotImplementedErroe("Not correct")
class Hourly(Employee):
    def __init__(self, name, empID):
        Employee.__init__(self, name, empID)
        self.hoursWorked = None
        self.payRate = None
    def calcSalary(self):
        self.hoursWorked = input("Weekly hours: ")
        self.payRate = input("What is the hourly rate: ")
        self.salary = int(self.hoursWorked)*float(self.payRate)*52
class Yearly(Employee):
    def __init__(self, name, empID):
        Employee.__init__(self, name, empID)
        self.years = None
        self.basePay = None
    def calcSalary(self):
        self.startingWage = input("Starting wage: ")
        self.years = input("Years Worked: ")
        self.salary = int(self.startingWage)+(int(self.startingWage)*.15*int(self.years))
 

employees = list()
employees.append(Hourly("Nathan",1))
employees.append(Yearly("Adriaunnah",2))
for emp in employees:
    emp.calcSalary()
    print("Name: ", emp.name," Salary: ", emp.salary)
