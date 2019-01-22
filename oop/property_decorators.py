class Employee:

    num_of_emp = 0
    raise_amount = 1.05

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        print('Delete name!')
        self.first_name = None
        self.last_name = None


emp_1 = Employee('Mike', 'Bannigs')
emp_2 = Employee('Joey', 'Tribbiani')

emp_1.full_name = 'Ross Geller'

print(emp_1.full_name)
print(emp_1.email)

del emp_1.full_name
print(emp_1.full_name)
