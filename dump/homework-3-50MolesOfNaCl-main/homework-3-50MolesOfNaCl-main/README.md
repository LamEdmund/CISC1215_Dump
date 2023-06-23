# Homework 3 (50 points)
Due Sunday, March 6 at 11:59 PM


## Problem 1: Area calculator refactor (20 points)

Refactor the iterative version of your area calculator so that it uses a `while` loop instead of a `for` loop. Write your program in `area_iterative.py`. The program must:

1. Repeatedly prompt the user for shapes and relevant dimensions.
2. Between each shape, ask the user if they want to add another one. Accept "y" and "n" as valid input. If the user enters an invalid value, ask again.
3. Present the total shape count and area.

Please look at these interaction examples carefully:

#### Successful interaction

```
Type of shape (circle, rectangle, or triangle): circle
Radius: 3
Enter another shape (y/n): y
Type of shape (circle, rectangle, or triangle): rectangle
Length: 2
Height: 3
Enter another shape (y/n): y
Type of shape (circle, rectangle, or triangle): triangle
Base: 9
Height: 3
Enter another shape (y/n): n
The total area of the 3 shape(s) is 47.77433388230814
```

#### Invalid "Enter another shape" prompt
```
Type of shape (circle, rectangle, or triangle): circle
Radius: 3
Enter another shape (y/n): test
Enter another shape (y/n): wrong
Enter another shape (y/n): n
The total area of the 1 shape(s) is 28.274333882308138
```

Automated testing will verify the final output is correct, and that the script can deal with bad "Enter another shape" prompts.


## Problem 2: `is_power()` (10 points)

Adapted from book exercise 6.4: An integer, `a`, is a power of `b` if both of the following are true:

* `a` is divisible by `b`
* `a/b` is a power of `b`.

Write a recursive function called `is_power()` that takes parameters `a` and `b` and returns `True` if `a` is a power of `b`, and `False` otherwise. Note: you will have to think about the base case.

Use the guardian pattern (see textbook p. 58) to require that `a` or `b` are integers. If `a` or `b` are not integers, your program should print an error and return nothing (`None`).

Write your solution in the file `is_power.py`. Please include test code showing that your `is_power()` function works by printing several example runs with different numbers. *Please add test code where indicated in the file:*

```
if __name__ == "__main__":
	# Write test code here
```

This will allow automated tests to check your function without interference from your test code. Automated testing will check several combinations of numbers and **most** error conditions.

## Written Questions (20 points)

1. Draw a stack diagram of `is_power(16, 2)`. (5 points)
2. Discuss `b == 1` as a special base case of the `is_power()` function. Do you need to check for it? What happens if your code does not account for situations where `b == 1`, and I call `is_power(10, 1)`? Why? (5 points)
3. Indicate whether a `for` or `while` loop would be a better way to solve the following problems, and explain why (10 points):
	1. Convert every letter in a string to upper-case, one by one.
	2. A game engine continuously checks for mouse and keyboard input.
	3. Access every apartment listing in Brooklyn, and calculate the average rent.
	4. A doctor's scheduling system sends reminders to all patients with appointments the next day.
	5. A subway train control system keeps the doors open until the conductor presses the "close" button.

## Rubric
* Area calculator (20 points)
	- Correct usage of loops (8 points)
	- Prompts for more shapes and deals with incorrect input (4 points)
	- Correct accumulation and output of area (3 points)
	- Correct shape counting (2 points)
	- Comments (3 points)
* `is_power()` (10 points)
	- Guardian pattern catches errors (2 points)
	- Correct identification of base case(s) (3 points)  
	- Correct recursive case (3 points)
	- Comments (2 points)
* Written questions (20 points)

## Submission

On Blackboard, please submit the following:

* A link to your repository
* Answers to the written questions