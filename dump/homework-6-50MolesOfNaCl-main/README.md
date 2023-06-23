# Homework 6 (50 points)
Due Wednesday, May 4 at 11:59:59 PM

## Problem 1: Employee and Company, procedural style (20 points)

This is a lab-style assignment where you will be making a specific set of improvements to an existing codebase rather than writing new code from scratch.

Look in `employee_procedural.py`. This file contains the beginnings of an employee management system. It is written in a procedural programming style, where the classes are minimal and objects are passed around through a set of functions. It already contains some functionality: you can create Employee and Company objects, and you can print Employee objects.

Maintaining the programming style shown in this file, add some new functions:

* Add an Employee to a Company. Do this in the `add_employee()` function shown on line 45.
* Pay an employee. To do this, increment the employee object's `amount_paid` by one month's pay (1/12 of the employee's salary). Do this in the `pay()` function shown on line 48.
* Pay all the employees in a company using the `pay()` function you just wrote. Do this in the `pay_all()` function shown on Line 51.
* Print information about a company: its name, the number of employees, and a list of every employee. Do this in the `print_company()` function shown on line 54.

As a final step, construct a Company object from employees in the text file `employees.txt`. Then pay everyone for one pay period and call `print_company()` on the Company object.

`employees.txt` contains data like this, representing an employee's ID number, name, and yearly salary:

```
3620132001 Reese 44650
```


The final output of your program should look something like this:


```
Computers Inc
99 employees
----------------------------------
ID: 3966957047, Name: Malik, Salary: 88064, YTD earnings: 7338.666666666667
ID: 5469018763, Name: Charlotte, Salary: 69205, YTD earnings: 5767.083333333333
ID: 8679516992, Name: Keshun, Salary: 44620, YTD earnings: 3718.3333333333335
ID: 5864773447, Name: Abraham, Salary: 60676, YTD earnings: 5056.333333333333
ID: 9477945650, Name: William, Salary: 53029, YTD earnings: 4419.083333333333
ID: 7597869359, Name: Travis, Salary: 67765, YTD earnings: 5647.083333333333
ID: 8242258245, Name: Emmalee, Salary: 87427, YTD earnings: 7285.583333333333
...
```

## Problem 2: Employee and Company, object-oriented style (20 points)

Take the code you wrote in Problem 1 and copy it into `employee_oop.py`. Refactor your code so that all functions are methods on the appropriate class. For example, the `print_employee()` will become a method on the Employee class, and your `add_employee()` function will become a method on the Company class.

Be sure to make all the necessary adjustments to each function's parameters and body as needed. Additionally, be sure to make use of Python's `__init__` special method for creating Employee and Company objects

Finally, adjust the code you wrote to read employees from a file so it works with this new system. Its output should be identical to the output from the previous problem.

## Written Questions (10 points)

1. Discuss the differences between your procedural and object-oriented code. From a functionality standpoint, is there any difference between them? Do you believe there is any reason to use one style over another? (5 points)
2. What if we wanted to make it so that some employees have a yearly salary, while some employees have an hourly rate? Discuss some possible ways of making this work. What changes would we need to make? (5 points)

## Grading
* Employee and Company, procedural style (20 points)
	- `add_employee()` (3 points)
	- `pay()` (3 points)
	- `pay_all()` (3 points)
	- `print_company()` (3 points)
	- Loading Employee data (5 points)
	- Comments (3 points)
* Employee and Company, object-oriented style (20 points)
	- Object-oriented conversion of Employee (5 points)
	- Object-oriented conversion of Company (5 points)
	- Conversion of Employee loading code (5 points)
	- Correct usage of `__init__` (2 points)
	- Comments (3 points)
* Written questions (10 points)

## Submission
On Blackboard, submit the following before the due date:

* A link to your GitHub repository.
* Responses to written questions.