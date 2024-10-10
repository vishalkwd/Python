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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employees=None):
        # passing None instead of empty list. Never pass mutable datatype as default args.
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name())


dev_1 = Developer('Mike', 'Bannigs', 50000, 'Python')
dev_2 = Developer('Joey', 'Tribbiani', 100000, 'Java')
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print('#########')
print(issubclass(Developer, Developer))
print(issubclass(Developer, Manager))
print(issubclass(Developer, Employee))
# print(help(Developer))  # Shows inheritance tree
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(mgr_1.email)
# mgr_1.print_emps()
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
