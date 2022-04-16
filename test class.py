

class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@yahoo.com'


    def fullName(self):
        print('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        print("Previous salary is ${}\n".format(self.pay))
        self.pay = int(self.pay * self.raise_amt)
        print("\nSalary after raise is: ${}".format(self.pay))



class Devoloper(Employee):
    raise_amt = 1.20
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    raise_amnt = 1.25
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employee.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employee.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print( emp.fullName())
    

emp1 = Employee('Rob', 'Mill', 70000)
emp2 = Devoloper('Matthew', 'Green', 70000, 'Python')

mgr_1 = Manager('Sue', 'Smith', 90000, [emp2])

mgr_1.print_emps()

