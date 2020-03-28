#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

import logging

# logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(asctime)s, %(filename)s, %(message)s")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class Employee:

    def __init__(self, fname, lname, age, address, salary):
        self.first_name = fname
        self.last_name = lname
        self.e_age = age
        self.e_salary = salary
        self.e_address = address

        logger.info("\nCreate Employee:\nName:\t{}\nEmail address:\t{}\nAddress:\t{}\nSalary:\t{}".format(self.fullname, self.email_address, self.e_address, self.e_salary))

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def email_address(self):
        return '{}.{}@mycompany.com'.format(self.first_name, self.last_name)

    @property
    def emp_salary(self):
        return self.e_salary

for i in range(1000):
    Employee("krishnendu","kayal",33,"EE-138/11, Salt Lake, Sector-2, Kolkata-700091",50000)
    Employee("Sanachari","kayal",33,"EE-138/11, Salt Lake, Sector-2, Kolkata-700091",50000)
    Employee("kamal","kayal",33,"Amratala, Salt Lake, Sector-2, Kolkata-700091",50000)
    Employee("indira","kayal",33,"Dhamuya, south 24 Pgs, , pin-356236",50000)