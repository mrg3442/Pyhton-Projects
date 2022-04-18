

class Employee:
    raise_amt = 1.05
    #defines attributes for employees class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@yahoo.com'

    #function to return  full name
    def fullName(self):
        print('{} {}'.format(self.first, self.last))
    #function to apply raise to salary and print before and after
    def apply_raise(self):
        print("Previous salary is ${}\n".format(self.pay))
        self.pay = int(self.pay * self.raise_amt)
        print("\nSalary after raise is: ${}".format(self.pay))



class Devoloper(Employee):
    raise_amt = 1.20
    #adds new attribute prog_lang and passes the creation of Parent attributes to old class to not reuse code
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


     #function to apply raise to salary and print before and after
    def apply_raise(self):
        print("Previous salary is ${}\n".format(self.pay))
        self.pay = int(self.pay * self.raise_amt)
        print("\nBecause you are a dev you get a extra raise!\n\
              New salary: ${}".format(self.pay))

class Manager(Employee):
    raise_amnt = 1.25
    #again adds new attribute employees and passes rest
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        #if no employees gives empty arr
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    #function to add employees to arr
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employee.append(emp)
    #removes employees from arr
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employee.remove(emp)
    #prints all employees belonging to this manager
    def print_emps(self):
        for emp in self.employees:
            print(emp.fullName())
    

emp1 = Employee('Rob', 'Mill', 70000)
emp2 = Devoloper('Matthew', 'Green', 70000, 'Python')

mgr_1 = Manager('Sue', 'Smith', 90000, [emp2])

emp1.apply_raise()
emp2.apply_raise()

