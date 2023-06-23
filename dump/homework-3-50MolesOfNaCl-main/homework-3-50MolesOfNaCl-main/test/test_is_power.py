import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from unittest.mock import patch

import is_power

failed = False
try:
    if is_power.is_power(10, 2):
        print("is_power(10, 2) should be false")
        failed = True
    if not is_power.is_power(8, 2):
        print("is_power(8, 2) should be true")
        failed = True
    if not is_power.is_power(100, 10):
        print("is_power(100, 10 should be true")
        failed = True
except Exception as e:
    raise Exception("One or more calls to is_power crashed", e)

if failed:
    raise Exception("One or more tests failed")
print("All tests passed")
