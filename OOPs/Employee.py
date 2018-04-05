class Employee:

    no_of_emp=0
    raise_amount=1.05

    def __init__(self, fname, lname, age, pay):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.pay=pay

        Employee.no_of_emp +=1

    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    def email(self):
        return "{}.{}@company.com".format(self.fname,self.lname)

    def raiseamount(self):
        self.pay = (self.pay*self.raise_amount)


e1=Employee("krishnendu", "kayal", 33, 90000)
e2=Employee("sanchari", "kayal", 29, 100000)
e1_name=e1.fullname()
e1_email=e1.email()
e1_raise=e1.raiseamount()
e2_name=e2.fullname()
e2_email=e2.email()
e2_raise=e2.raiseamount()
print(e1_name)
print(e2_name)
print(e1_email)
print(e2_email)
print(e2.pay)
print(e1.pay)
print(Employee.no_of_emp)
