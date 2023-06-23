import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from unittest.mock import patch

import is_power

failed = False

try:
    if is_power.is_power("10", 2) is not None:
        raise Exception()
except:
    print("FAILED: is_power('10', 2) should return nothing")
    failed = True

try:
    if is_power.is_power(10, "2") is not None:
        raise Exception()
except:
    print("FAILED: is_power(10, '2') should return nothing")
    failed = True

if failed:
    raise Exception("One or more tests failed")
print("All tests passed")
