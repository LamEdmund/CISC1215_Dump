import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from unittest.mock import patch

import employee_oop as employee_oop

print()
failed = False
try:
    print("Testing paying employees...")
    e = employee_oop.Employee(1234, 'test', 12)
    e.pay()
    if e.amount_paid != 1:
        print("...Employee not being paid")
        failed = True
    else:
        print("...Employee was paid correctly")

    print("Testing paying bonus employees...")
    e = employee_oop.BonusEmployee(1234, 'test', 12, 1)
    for i in range(12):
        e.pay()
    if e.amount_paid == 12:
        print("...BonusEmployee is not getting their bonus :(")
        failed = True
    elif e.amount_paid != 13:
        print("...BonusEmployee is not being paid correctly")
        failed = True
    else:
        print("...BonusEmployee was paid their salary and bonus")
    
    print("Testing adding employees to company...")
    c = employee_oop.Company("Test")
    c.add_employee(e)
    if len(c.employees) != 1:
        print("...Employee not added to company")
        failed = True
    else:
        print("...Employee was added to company")
    

    print("Testing paying all employees...")
    e1 = employee_oop.Employee(1234, 'test1', 12)
    e2 = employee_oop.Employee(1234, 'test2', 24)
    c = employee_oop.Company("Test")

    c.add_employee(e1)
    c.add_employee(e2)

    c.pay_all()

    if c.employees[0].amount_paid != 1 or c.employees[1].amount_paid != 2:
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
