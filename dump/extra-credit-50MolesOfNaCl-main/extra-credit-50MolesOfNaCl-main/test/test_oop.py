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

    print("Testing paying contracted employees...")
    e = employee_oop.ContractEmployee(1234, 'test', 12, 1)
    e.pay()

    excepted = False
    try:
        e.pay()
    except:
        excepted = True

        if e.amount_paid == 1:
            print("...ContractEmployee successfully prevents paying after the contract end")
        elif e.amount_paid != 1:
            print("...ContractEmployee correctly raised an exception, but was not paid the right amount!")
            failed = True
    
    if not excepted:
            print("...ContractEmploye did not raise an exception for too much pay!")
            failed = True
    
    print("Testing adding employees to company...")
    c = employee_oop.Company("Test")

    c.add_employee(e)
    if len(c.employees) != 1:
        print("...Employee not added to company")
        failed = True
    else:
        print("...Employee was added to company")
    

    print("Testing paying all employees...")
    e = employee_oop.ContractEmployee(1234, 'test', 12, 1)
    c = employee_oop.Company("Test")

    c.add_employee(e)

    try:
        c.pay_all()
        c.pay_all()
    except:
        print("...paying all employes falied! pay_all() raised an exception when it should not have!")
        failed = True
        
    if e.amount_paid == 1:
        print("...All employees are being paid")
    else:
        print("...Employees are not being paid correctly")
        failed=True

except Exception as e:
    raise Exception("One or more tests crashed", e)

print()
if failed:
    raise Exception("One or more tests failed")
print("All tests passed")
