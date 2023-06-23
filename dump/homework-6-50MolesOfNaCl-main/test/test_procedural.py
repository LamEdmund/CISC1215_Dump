import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from unittest.mock import patch

import employee_procedural

print()
failed = False
try:
    print("Testing paying employees...")
    e = employee_procedural.make_employee(1234, 'test', 12)
    employee_procedural.pay(e)
    if e.amount_paid != 1:
        print("...Employee not being paid")
        failed = True
    else:
        print("...Employee was paid correctly")
    
    print("Testing adding employees to company...")
    c = employee_procedural.make_company("Test")
    employee_procedural.add_employee(e, c)
    if len(c.employees) != 1:
        print("...Employee not added to company")
        failed = True
    else:
        print("...Employee was added to company")
    

    print("Testing paying all employees...")
    e1 = employee_procedural.make_employee(1234, 'test1', 12)
    e2 = employee_procedural.make_employee(1234, 'test2', 24)
    c = employee_procedural.make_company("Test")

    employee_procedural.add_employee(e1, c)
    employee_procedural.add_employee(e2, c)

    employee_procedural.pay_all(c)

    if c.employees[0].amount_paid != 1 or c.employees[1].amount_paid != 2:
        print(c.employees[0].print_employee())
        print(c.employees[1].print_employee())
        print("...Not all employees in a company are being paid!")
        failed = True
    else:
        print("...All employees are being paid")

except Exception as e:
    raise Exception("One or more tests crashed", e)

print()
if failed:
    raise Exception("One or more tests failed")
print("All tests passed")
