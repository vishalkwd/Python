import datetime


class Employee:

    num_of_emp = 0
    raise_amount = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@email.com'

        Employee.num_of_emp += 1

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  # Class methods can be used as alternative constructors.
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Creating a new class method/constructor to create instance from a string eg. emp_str_1
    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Mike', 'Bannigs', 50000)
emp_2 = Employee('Joey', 'Tribbiani', 100000)
####
# print(emp_1.raise_amount)
# emp_1.set_raise_amount(1.5)  # When this is called it sets the variable for all instances
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
####

# Class Method exmple
emp_str_1 = 'John-Joe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

emp_new_1 = Employee.from_string(emp_str_1)
print(emp_new_1.pay)

# Static method example starts here
my_date = datetime.date(2019, 1, 21)

print(Employee.is_workday(my_date))
