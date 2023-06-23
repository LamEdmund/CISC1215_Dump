# Homework 5 (50 points)
Due Tuesday, April 12 at 11:59:59 PM

## Problem 1: Word of the Day (20 points)

Write a program that generates a word of the day and prints it out. Choose from the words in the `words.txt` file. The rules for picking a word are as follows:

* The word should start with a letter corresponding with the day of the month. So the word of the first day of the month should start with "a", then the 2nd is "b", then the 3rd is "c", and so on.
* Once you exhaust all letters, loop around. So the 26th day of the month should start with "z", then the 27th should start with "a", and continue from there.
* The first letter of the word is all that matters. Once you have chosen an appropriate first letter, you can choose the word at random.

Some hints:

You will want to organize the words in `words.txt` into a dictionary that maps a letter to a list of words starting with that letter.

You can choose a random element from a list with the `random.choice()` function. To use it, you must import the `random` module.

You can get the current day of the month by importing the `datetime` module, then accessing it with `datetime.datetime.today().day`.

Automated testing expects your word selector to be written in the function `get_word_of_the_day()`. The function accepts a day of the month as an argument, and returns an appropriate word for that day.

Do you work in the `word_of_the_day.py` file.

## Problem 2: Removing Duplicates (20 points)

Write a destructive function `remove_duplicates()` that accepts a list as an argument, then removes duplicate elements from the list.

As an example, here is what using your function in interactive mode will look like:

```
>>> a = [1, 2, 3, 4, 5, 5, 6]
>>> remove_duplicates(a)
>>> a
[1, 2, 3, 4, 5, 6]

>>> b = [5, 1, 2, 3, 4, 5, 5, 6]
>>> remove_duplicates(b)
>>> b
[1, 2, 3, 4, 5, 6]

>>> c = [2, 3, 4, 5, 6]
>>> remove_duplicates(c)
>>> c
[2, 3, 4, 5, 6]
```

Automated testing will evaluate your function with a variety of inputs. The specific item you choose to remove doesn't matter, so long as the final list only contains one of each element.

If you are familiar with Python sets, do not use them as part of completing this problem.

Do your work in `remove_duplicates.py`.


## Written Questions (10 points)

1. Describe why your `remove_duplicates()` function is destructive. How could you change it so that it is non-destructive? Be specific. (5 points)

2. Discuss the implications of refactoring your `remove_duplicates()` function so that it accepts a tuple as an argument instead of a list, but is otherwise unchanged. Is this possible? Why or why not? What would you have to change about how the function works to make it possible to accept a tuple as an argument? Be as specific as possible when describing what you would change. (5 points)

## Grading
* Word of the Day (20 points)
	- Calls `word_of_the_day()` with current day and prints the result (3 points)
	- Correct character-to-list dictionary mapping (5 points)
	- `word_of_the_day()` correctly picks the day's starting letter (5 points)
	- Looping around functionality (2 points)
	- Randomly selects word with correct starting letter (2 points)
	- Comments (3 points)
* Remove duplicates (20 points)
	- Function uses destructive list operations (5 points)
	- Function itself is destructive (5 points)
	- Correct duplicate tracking (5 points)
	- Test cases (2 points)
	- Comments (3 points)


## Submission
On Blackboard, submit the following before the due date:

* A link to your GitHub repository.
* Responses to written questions.