import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from unittest.mock import patch

import palindrome

print()
failed = False
try:
    print('Testing "able was i ere i saw elba"...')
    if not palindrome.is_palindrome("able was i ere i saw elba"):
        print('"able was i ere i saw elba" was False, but should be True!')
        failed = True
    else:
        print("...passed")
    
    print()
    print('Testing "nope not a palindrome"...')
    if palindrome.is_palindrome("nope not a palindrome"):
        print('"nope not a palindrome" was True, but should be False')
        failed = True
    else:
        print("...passed")

    print()
    print('Testing "was it a    car or a cat i saw"...')
    if not palindrome.is_palindrome("was it a    car or a cat i saw"):
        print('"was it a    car or a cat i saw" was False, but should be True')
        failed = True
    else:
        print("...passed")

except Exception as e:
    raise Exception("One or more calls to is_palindrome crashed", e)

print()
if failed:
    raise Exception("One or more tests failed")
print("All tests passed")
