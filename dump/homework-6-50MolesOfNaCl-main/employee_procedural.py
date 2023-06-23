class Employee:
    """A class representing an employee at a company"""
    id = None
    name = None
    salary = 0
    amount_paid = 0
    def __init__(self, id, name, salary, amount_paid):  
        self.id = id
        self.name = name
        self.salary = salary
        self.amount_paid = amount_paid
    #overload constructor
    def __init__(self):
        pass

class Company:
    """A class representing a company"""
    name = None
    employees = None
    def __init__(self, name, employees):  
        self.name = name
        self.employees = employees
    #overload constructor
    def __init__(self):
        pass
    
def make_employee(id, name,salary):
    """
        Create a new employee object. All employees have
        an employee ID, a name, and a yearly salary.
        Additionally, objects keep track of how much the
        employee has been paid so far.
    """
    e = Employee()

    e.id = id
    e.name = name
    e.salary = (int)(salary) #Python would assume string otherwise

    # Amount paid defaults to 0 - the employee has not
    # been paid anything yet.
    e.amount_paid = 0

    return e

def make_company(name):
    """
        Create a new Company object. All companies have a name and
        a list of employees.
    """
    c = Company()

    c.name = name       # Company name
    c.employees = []    # List of all employees

    return c

# TODO: Add an employee to a company
def add_employee(employee, company):
    company.employees.append(employee)

def print_employee(e):
    print(f"ID: {e.id}, Name: {e.name}, Salary: {e.salary}, YTD earnings: {e.amount_paid}")

# TODO: Pay an employee for one pay period
def pay(employee):
    employee.amount_paid += (employee.salary/12)

# TODO: Pay all employees in a company
def pay_all(company):
    for employee in company.employees:
        pay(employee)

# TODO: Print information about a company
def print_company(company):
    print(company.name)
    print(len(company.employees)," employees \n----------------------------------")
    for employee in company.employees:
        print_employee(employee)

# entry
if __name__=="__main__":
    c = make_company("Computers Inc")
    file = open("employees.txt")
    for line in file:
        strings = line.split()
        add_employee(make_employee(strings[0],strings[1],strings[2]), c)
    file.close()
    
    # boop
    pay_all(c)
    print_company(c)