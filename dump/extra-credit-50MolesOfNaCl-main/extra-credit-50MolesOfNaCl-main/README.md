# Extra Credit (20 points)
Optionally due Sunday, May 22 at 11:59:59 PM

## Employee and Company with Exceptions

This is a lab-style assignment where you will be making a specific set of improvements to an existing codebase rather than writing new code from scratch. You may find the [table tennis repository](https://github.com/CUNY-CISC1215-Spring2022/exceptions-inheritance) to be a useful model.

Copy your `employee_oop.py` file from the previous assignment (either 6 or 7) into this one. If you are unsure if your previous employee code works correctly, you may contact me for assistance in fixing any issues.

Your company now wishes to track a new type of employee: one who is hired temporarily. This employee will be contracted for a set number of months, after which the contract ends and the employee cannot be paid anymore.

Using inheritance, create a new type of Employee, called `ContractEmployee`, that is a child class of `Employee`.

Implement the following functionality in the `ContractEmployee` class:

* Unlike an `Employee`, a `ContractEmployee` is created with an id, name, effective yearly salary, and the duration of their contract in months.
* Unlike an `Employee`, a `ContractEmployee` keeps track of how many times it has been paid.
* After the `ContractEmployee` has been paid through their alotted number of pay periods, the `ContractEmployee` object should _prevent the employee from being paid again_.
* Printing a `ContractEmployee` should include the number of months remaining in their contract.

Use exceptions to prevent the `ContractEmployee` from being paid more than they should. In other words, if someone tries to call `pay()` on a `ContractEmployee` object once it has run out of pay periods, the `ContractEmployee` object should raise an `Exception` with a suitable message.

Revisit your employee loading code. In Computers Inc., everyone whose ID ends in a 8 is a contracted employee for a 3-month term. Alter your code to support this, then pay all your employees 4 times. Have your Company object catch the exception in `pay_all()`, and have the Company track how many times paying has failed.

Here is example output after paying 4 times (note that this includes bonus amounts - including this is optional!):

```
Computers Inc
99 employees
15 pay failures
-------------------------------------
ID: 3966957047, Name: Malik, Salary: 88064, YTD earnings: 29354.666666666668
ID: 5469018763, Name: Charlotte, Salary: 69205, YTD earnings: 23068.333333333332
ID: 8679516992, Name: Keshun, Salary: 44620, YTD earnings: 14873.333333333334
ID: 5864773447, Name: Abraham, Salary: 60676, YTD earnings: 20225.333333333332
ID: 9477945650, Name: William, Salary: 53029, YTD earnings: 17676.333333333332
ID: 7597869359, Name: Travis, Salary: 67765, Bonus: 1500, YTD earnings: 22588.333333333332
ID: 8242258245, Name: Emmalee, Salary: 87427, YTD earnings: 29142.333333333332
ID: 1552900251, Name: Ethan, Salary: 79494, YTD earnings: 26498.0
ID: 2128364000, Name: Angel, Salary: 71689, YTD earnings: 23896.333333333332
ID: 3117072108, Name: Nina, Salary: 43278, Remaining: 0, YTD earnings: 10819.5
```

## Rubric
* ContractEmployee child class structure and implementation (4 points)
* Correct exception raising in pay() (5 points)
* Correct exception handling (5 points)
* Updated output with months remaining and error count (4 points)
* Comments (2 points)

## Submission
On Blackboard, submit the following before the due date:

* A link to your GitHub repository.