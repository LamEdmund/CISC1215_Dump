import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from unittest.mock import patch

import word_of_the_day

print()
failed = False
try:
    print('Testing get_word_of_the_day(1)...')
    word = word_of_the_day.get_word_of_the_day(1)
    if not word[0] == 'a':
        print('get_word_of_the_day(1) should start with "a", but it starts with ' + word[0])
        failed = True
    else:
        print('...get_word_of_the_day(1) correctly starts with "a"')

    print('Testing get_word_of_the_day(28)...')
    word = word_of_the_day.get_word_of_the_day(28)
    if not word[0] == 'b':
        print('get_word_of_the_day(28) should start with "b", but it starts with ' + word[0])
        failed = True
    else:
        print('...get_word_of_the_day(28) correctly starts with "b"')

except Exception as e:
    raise Exception("One or more calls to word_of_the_day() crashed", e)

print()
if failed:
    raise Exception("One or more tests failed")
print("All tests passed")
