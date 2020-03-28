#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

class Employee:
    number_of_employee=0

    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
        Employee.number_of_employee +=1

    def displayname(self):
        print("Employee Name is ", self.name)

    def displayage(self):
        print("Employee Age is", self.age)

    def employeesalary(self):
        print("This is Employee salary", self.salary)

    def noofemployeee(self):
        print("No of Employee is", Employee.number_of_employee)


e1=Employee("krishsnendu",25,20000)
e2=Employee("babu",21,200000)
e1.displayname()
e1.displayage()
e1.employeesalary()
e1.noofemployeee()
e2.displayname()
e2.displayage()
e2.employeesalary()
e2.noofemployeee()
