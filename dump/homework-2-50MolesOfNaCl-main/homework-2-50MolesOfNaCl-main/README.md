# Homework 2 (50 points)
Due Sunday, February 27 at 11:59 PM


## Shape Area Calculator (40 points)

In this assignment, you will combine everything we have learned so far to create a geometric calculator that sums the area of many shapes.

As part of this assignment, you will use the `input()` function. To assist you, the initial `input()` call is written for you in the `area_iterative.py` and `area_recursive.py` files.

### Task
Write a program that calculates the total area of several geometric shapes. The program must:

1. Ask the user how many shapes there are.
2. For each shape, ask the user what kind of shape it is, then request the appropriate measurements.
3. Once all shape information has been obtained, calculate the total area of the shapes and print it.

Your calculator should support computing the area of circles, squares, and triangles.

Please write this calculator *twice*: once using iteration with a `for` loop, and once using recursion.

Write your iterative implementation with a `for` loop in `area_iterative.py`, and your recursive implementation in `area_recursive.py`.

Here is what interacting with your program should look like:

```
How many shapes? 3
Type of shape (circle, rectangle, or triangle): circle
Radius: 3
Type of shape (circle, rectangle, or triangle): rectangle
Length: 2
Height: 3
Type of shape (circle, rectangle, or triangle): triangle
Base: 9
Height: 3
The total area is 47.77433388230814
```

**Your program may assume that the user-inputted shape type is always correct**. You _do not_ need to check for user error (i.e., someone types "circel" instead of "circle").

The tests (available in the Actions tab) will verify that running the program according to the script above works correctly. Please note that if your program produces slightly different output then what is shown, it may fail tests.

## Written Questions (10 points)

1. Discuss your implementations of the area calculator. In your opinion, which approach (recursion or a `for` loop) is the better method of solving this problem? Why? (4 points)
2. Draw a stack diagram of a hypothetical run of your recursive implementation with two circles. (4 points)
3. In class, we discussed the built-in `math` Python module. Consult the Python documentation and find another module that looks interesting to you. Briefly describe what it is for and what kinds of functionality it provides (2 points).

## Rubric
* Iterative area calculator (20 points)
	- Usage of a `for` loop with the `range()` function (5 points)
	- Correct conditionals with different area calculations (5 points)
	- Correct accumulation and output of area (5 points)
	- Correct area calculation (2 points)
	- Comments (3 points)
* Recursive area calculator (20 points)
	- Recursive function structure with base and recursive cases (5 points)
	- Correct conditionals with different area calculations (5 points)
	- Correct accumulation and output of area (5 points)
	- Correct area calculation (2 points)
	- Comments (3 points)
* Written questions (10 points)

## Submission

On Blackboard, please submit the following:

* A link to your repository
* Answers to the written questions