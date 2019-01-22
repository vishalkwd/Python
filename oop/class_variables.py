class Employee:

    num_of_emp = 0
    raise_amount = 1.05
    __private_var = 100

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


emp_1 = Employee('Mike', 'Bannigs', 50000)
emp_2 = Employee('Joey', 'Tribbiani', 100000)
# print(Employee.num_of_emp)

print(Employee.__module__)
print(emp_1._Employee__private_var)
