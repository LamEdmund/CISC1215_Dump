class Employee:
    """A class representing an employee at a company"""
    id = None
    name = None
    salary = 0
    amount_paid = 0
    
    def __init__(self, id, name, salary):  
        self.id = id
        self.name = name
        self.salary = (int)(salary)
    def print_employee(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}, YTD earnings: {self.amount_paid}")
    def make_employee(id, name,salary):
        """
            Create a new employee object. All employees have
            an employee ID, a name, and a yearly salary.
            Additionally, objects keep track of how much the
            employee has been paid so far.
        """

        id = id
        name = name
        salary = (int)(salary) #Python would assume string otherwise

        # Amount paid defaults to 0 - the employee has not
        # been paid anything yet.
        amount_paid = 0
        # TODO: Pay an employee for one pay period
    def pay(self):
        self.amount_paid += (self.salary/12)


class Company:
    """A class representing a company"""
    name = None
    employees = []
    def __init__(self, name):  
        self.name = name
    # TODO: Add an employee to a company
    def add_employee(self,employee):
        self.employees.append(employee)
    def make_company(self, name):
        """
            Create a new Company object. All companies have a name and
            a list of employees.
        """
        name = name       # Company name
        employees = []    # List of all employees

    # TODO: Pay all employees in a company
    # SOME PEOPLE ARE NOT BEING PAID
    # Mystery solved, NULL value shows up in test for some reason
    def pay_all(self):
        for employee in self.employees:
            employee.pay()

    # TODO: Print information about a company
    def print_company(self):
        print(self.name)
        print(len(self.employees)," employees \n----------------------------------")
        for employee in self.employees:
            employee.print_employee()

# entry
if __name__=="__main__":
    c = Company("Computers Inc")
    file = open("employees.txt")
    for line in file:
        strings = line.split()
        e = Employee(strings[0],strings[1],strings[2])
        c.add_employee(e)
    file.close()
    
    #Boop
    c.pay_all()
    c.print_company()