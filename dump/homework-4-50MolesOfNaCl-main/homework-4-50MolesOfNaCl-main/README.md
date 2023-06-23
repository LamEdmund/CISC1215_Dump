# Homework 4 (50 points)
Due Monday, March 21 at 11:59:59 PM

## Problem 1: Palindrome with Spaces (20 points)

In class, we wrote a recursive function `is_palindrome()` that is capable of determining if a given string is a palindrome (i.e., the string is identical to itself backwards).

The following single-word strings are palindromes:

```
"tacocat"
"racecar"
"zzzz" 
""
"a"
```

However, sentences can be palindromes. Here are some examples:

```
"Able was I ere I saw Elba."
"A man, a plan, a canal – Panama!"
"A Toyota. Race fast, safe car. A Toyota."
```

**Alter [the is_palindrome() function we designed in class](https://github.com/CUNY-CISC1215-Spring2022/lecture-8/blob/main/palindrome.py) so that it accounts for any number of spaces in the input. You may assume that all strings passed into the function do not contain punctuation and have been lower-cased in advance:**

```
"able was i ere i saw elba": True
"a man a plan a canal panama": True
"a toyota    race fast safe car a toyota": True
"the ships hung in the sky in much the same way that bricks dont": False
```

Your new function should be recursive. Limit string functionality to relational operators, indexing, slicing, `in`, and concatenation. **Do not use built-in string methods or any additional Python modules**. Please include additional test cases demonstrating that your function works.

Automated tests assume the `palindrome.py` file contains an `is_palindrome()` function.

## Problem 2: Shortest and Longest Palindromes (18 points)

Use your `is_palindrome()` function to find the shortest and longest palindromes in `words.txt`. In your program, create two lists: one that contains the shortest palindromes, and one that contains the longest palindromes. Once your program is complete, print the lists.

Do your work in `palindrome_stats.py`. You may copy `is_palindrome()` into `palindrome_stats.py`.

Output:

```
Shortest: ["aa"] 
Longest: ["deified", "halalah", "reifier", "repaper", "reviver", "rotator", "sememes"]
```

Please limit string functionality to relational operators, indexing, slicing, `in`, and concatenation. **Do not use built-in string methods or any additional Python modules.**

*There is no automated testing for this file beyond ensuring that it runs and does not crash.* You will know it works when the output looks like the output shown above.

## Written Questions (12 points)

1. Draw a stack diagram of your new recursive `is_palindrome()` function with `"ufo tofu"` as input. (5 points)
2. `words.txt` is appropriate for finding palindromes because its creator ensured all words are lower-case and do not contain punctuation. Imagine we downloaded a different wordlist where its creator had not cleaned it up (for example, [this 4 megabyte list of 400,000 words](https://raw.githubusercontent.com/dwyl/english-words/master/words.txt)). Consult the [Python string documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), describe any methods you find that might be helpful for eliminating undesirable characters like punctuation, and explain how you would use them. (3 points)
4. Show how to use slicing to extract the following substrings from `"mango"` under the given conditions. Alternatively, indicate whether the given conditions are impossible (4 points):
	1. `"ngo"` (positive start, positive end)
	2. `"go"` (positive start, negative end)
	3. `"ang"` (negative start, positive end)
	4. `"man"` (negative start, negative end)


## Grading

* Palindrome with Spaces (20 points)
	- Correct identification and handling of spaces (5 points)
	- Still works with single-word palindromes (4 points)
	- Does not use string methods (4 points)
	- Correct base case(s) (2 points)
	- Correct recursive case(s) (2 points)
	- Test cases (1 point)
	- Comments (2 points)
* Shortest and Longest Palindromes (18 points)
	- Correct tracking of the longest/shortest palindromes (5 points)
	- Correct identification of a shorter/longer palindrome (5 points)
	- Correct accumulation of longest and shortest palindromes words (5 points)
	- Comments (3 points)
* Written responses (12 points)

## Submission
On Blackboard, submit the following before the due date:

* A link to your GitHub repository.
* Responses to written questions.