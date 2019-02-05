'''
example of creating class, sub-class, instance ...
'''


# super class ------------------------------------------------
class Employee:

    # class variable, can be accessed by either "Employee." or "self."
    # updating class variable through one instance will not
    # change the class variable value for the class or other instances
    raise_amount = 1.05
    employee_number = 0

    # special method (dunder)
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + "." + last + "@email.com"
        Employee.employee_number += 1 # increment when creating an instance

    # called if __str__ is not defined
    def __repr__(self):
        return "Employee: {} {}".format(self.first, self.last)


    def __str__(self):
        return "{} {}, {}".format(self.first, self.last, self.email)

    def __add__(self, other):
        return float(self.pay) + float(other.pay)


    # regular method automatically takes the instance
    # as the first argument (by convention called self)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    # with the property decorator, one can
    # access the method like an attribute
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name !")
        self.first = None
        self.last = None


    # class method takes the class as the first argument (cls)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


    # static method doesn't pass instance nor class
    @staticmethod
    def is_workday(day):
        if day == 5 or day== 6:
            return False
        return True



# sub-class --------------------------------------------------
class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first, last, pay, language):
        # call parent __init__ method
        super().__init__(first, last, pay)
        # one can also use:
        # Employee.__init__(self, first, last, pay)
        self.language = language


class Manager(Employee):

    # Do not pass mutable data type as default
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rm_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print("-->", emp.fullname)



# using the classes ------------------------------------------
emp_1 = Employee("John", "Smith", 50000)
emp_str_2 = "Steve-Doe-70000"
emp_2 = Employee.from_str(emp_str_2)
today = 3
emp_1.fullname = "Matthew Smith"

dev_1 = Developer("Andy", "Lee", 80000, "Python")
dev_2 = Developer("Mike", "Hu", 80000, "Java")
mgr_1 = Manager("Sue", "Smith", 95000, [dev_1])
mgr_1.add_employee(dev_2)



# output -----------------------------------------------------
print(emp_1)
print(emp_2)
print(emp_1 + emp_2)
print(Employee.is_workday(today))

print(dev_1)
print(mgr_1.print_employee())
print(issubclass(Developer, Employee))
print(isinstance(mgr_1, Developer))

print(Employee.employee_number)



