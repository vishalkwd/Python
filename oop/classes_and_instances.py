# Python Object-Oriented Programming


class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@email.com'

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


employee_1 = Employee('Mike', 'Bannigs', '50000')
employee_2 = Employee('Joey', 'Tribbiani', '100000')

print(employee_1.full_name())
print(Employee.full_name(employee_2))
