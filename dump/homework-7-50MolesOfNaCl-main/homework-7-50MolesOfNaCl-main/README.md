# Homework 7 (40 points)
Due Monday, May 16 at 11:59:59 PM

## Employee and Company with Inheritance (30 points)

This is a lab-style assignment where you will be making a specific set of improvements to an existing codebase rather than writing new code from scratch. You may find the [table tennis repository](https://github.com/CUNY-CISC1215-Spring2022/exceptions-inheritance) to be a useful model.

Copy your `employee_oop.py` file from the previous assignment into this one. If you are unsure if your previous employee code works correctly, you may contact me for assistance in fixing any issues.

Your company now wishes to track a new type of employee: one who is salaried, but receives a bonus at the end of every 12-month period.

Using inheritance, create a new type of Employee, called `BonusEmployee`, that is a child class of `Employee`.

Using overriding or extending, implement the following functionality in the `BonusEmployee` class:

* Unlike an `Employee`, a `BonusEmployee` is created with an id, name, yearly salary, and a yearly bonus.
* Unlike an `Employee`, a `BonusEmployee` keeps track of how many times it has been paid.
* On the 12th pay period, the `BonusEmployee` is paid the bonus in addition to the normal salary.
* Bonuses should be paid _every 12 payments_ (the 12th, 24th, 36th, etc).
* Printing a BonusEmployee should include the yearly bonus.

Revisit your employee loading code. In Computers Inc., everyone whose ID ends in a 9 receives a yearly bonus of $1,500.

```
Computers Inc
99 employees
----------------------------------
ID: 3966957047, Name: Malik, Salary: 88064, YTD earnings: 7338.666666666667
ID: 5469018763, Name: Charlotte, Salary: 69205, YTD earnings: 5767.083333333333
ID: 8679516992, Name: Keshun, Salary: 44620, YTD earnings: 3718.3333333333335
ID: 5864773447, Name: Abraham, Salary: 60676, YTD earnings: 5056.333333333333
ID: 9477945650, Name: William, Salary: 53029, YTD earnings: 4419.083333333333
ID: 7597869359, Name: Travis, Salary: 67765, Bonus: 1500, YTD earnings: 5647.083333333333
ID: 8242258245, Name: Emmalee, Salary: 87427, YTD earnings: 7285.583333333333
```

## Written questions (10 points)

1. Where did you use extending? Where did you use overriding? Discuss why you chose the approaches you did. (5 points)
2. Revisit Question 2 from Homework 6. What if we wanted to make it so that some employees have an hourly rate instead of a yearly salary (i.e., we make an HourlyEmployee class). Discuss whether overriding or extending the Employee methods would be more appropriate here. (5 points)

## Grading
* Employee and Company with Inheritance (30 points)
	- BonusEmployee functionality
		+ Store fixed bonus amount (4 points)
		+ Track number of times paid (4 points)
		+ Pay bonus every 12 pay periods (4 points)
		+ Print bonus amount (4 points)
	- Correct override/extend functionality (5 points)
	- Revising employee loading code (6 points)
	- Comments (3 points)
* Written questions (10 points)

## Submission
On Blackboard, submit the following before the due date:

* A link to your GitHub repository.
* Responses to written questions.