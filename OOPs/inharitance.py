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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount =  amount

    @classmethod
    def from_scring(cls, emp_str):
        first, last, pay = emp_str.split("-")
        cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() ==5 or day.weekday()==6:
            return False
        return True
class Developer(Employee):
    raise_amount=1.10
    def __init__(self, fname, lname, age, pay, prog_lang):
        super().__init__(fname, lname, age, pay)
        self.prog_lang=prog_lang
        #Employee.__init__(self, fname, lname, age, pay) --> This is another way to copy instance



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

d1=Developer("krishnendu", "kayal", 33, 90000, "C++")
d2=Developer("sanchari", "kayal", 29, 100000, "Java")
print(d1.email())
print(d2.email())
#print(help(Developer))
print(d1.pay)
d1.raiseamount()
print(d1.pay)
print(d1.email())
print(d1.prog_lang)
print(d2.email())
print(d2.prog_lang)
