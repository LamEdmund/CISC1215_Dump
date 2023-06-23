import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from unittest.mock import patch

print(
    "Iterative: Should compute an area of 47.77433388230814 from test input with bad y/n responses"
)
asdf = None
with patch(
    "builtins.input",
    side_effect=[
        "circle",
        3,
        "y",
        "rectangle",
        2,
        3,
        "z",
        "y",
        "triangle",
        9,
        3,
        "asdf",
        "n",
    ],
) as input_patch:
    with patch("builtins.print") as print_patch:
        import area_iterative

        asdf = print_patch

        found_area = False
        for call in print_patch.call_args_list:
            if "47.77433388230814" in str(call):
                found_area = True
                break

        if not found_area:
            raise Exception("Expected area of 47.77433388230814 to be found in output")
print("OK")
