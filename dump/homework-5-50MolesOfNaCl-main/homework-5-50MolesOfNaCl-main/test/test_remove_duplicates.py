import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from unittest.mock import patch

import remove_duplicates

print()
failed = False
try:
    print("Testing that [1, 2, 3] is unchanged...")
    a = [1, 2, 3]
    remove_duplicates.remove_duplicates(a)
    if not (1 in a and 2 in a and 3 in a and len(a) == 3):
        print('...remove_duplicates incorrectly modified a list with no duplicates!')
        failed = True
    else:
        print('...remove_duplicates correctly did not modify a list with no duplicates')

    print("Testing that [1, 2, 1] has duplicates removed...")
    a = [1, 2, 1]
    remove_duplicates.remove_duplicates(a)
    if not (1 in a and 2 in a and len(a) == 2):
        print('...remove_duplicates did not remove duplicates!')
        failed = True
    else:
        print('...remove_duplicates correctly removed duplicates')

    print("Testing that [1, 2, 1, 1] has all duplicates removed...")
    a = [1, 2, 1, 1]
    remove_duplicates.remove_duplicates(a)
    if not (1 in a and 2 in a and len(a) == 2):
        print('...remove_duplicates did not remove all duplicates!')
        failed = True
    else:
        print('...remove_duplicates correctly removed all duplicates')

except Exception as e:
    raise Exception("One or more calls to remove_duplicates() crashed", e)

print()
if failed:
    raise Exception("One or more tests failed")
print("All tests passed")
