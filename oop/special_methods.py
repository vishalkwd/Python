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

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay


emp_1 = Employee('Mike', 'Bannigs', 50000)
emp_2 = Employee('Joey', 'Tribbiani', 100000)
print(emp_1.__repr__())
print(repr(emp_1))
print(emp_2.__str__())
print(str(emp_2))
print(emp_1 + emp_2)
