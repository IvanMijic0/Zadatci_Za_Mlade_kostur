import unittest
from io import StringIO
import sys
from typing import List

from tasks.task7.printDiamondPattern import printDiamondPattern


class TestDiamondPattern(unittest.TestCase):
    def capture_output(self, func, *args) -> List[str]:
        # Helper method to capture the printed output of a function
        saved_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = saved_stdout
        return captured_output.getvalue().strip().split('\n')

    def test_diamond_pattern5(self):
        expected_output = [
            "*",
            "* *",
            "* * *",
            "* * * *",
            "* * * * *",
            "* * * *",
            "* * *",
            "* *",
            "*"
        ]
        rows = 5

        captured_output = self.capture_output(printDiamondPattern, rows)
        captured_output_lines = [line.strip() for line in captured_output]
        self.assertEqual(captured_output_lines, expected_output)

    def test_diamond_pattern9(self):
        expected_output = [
            "*",
            "* *",
            "* * *",
            "* * * *",
            "* * * * *",
            "* * * * * *",
            "* * * * * * *",
            "* * * * * * * *",
            "* * * * * * * * *",
            "* * * * * * * *",
            "* * * * * * *",
            "* * * * * *",
            "* * * * *",
            "* * * *",
            "* * *",
            "* *",
            "*"
        ]
        rows = 9

        captured_output = self.capture_output(printDiamondPattern, rows)
        captured_output_lines = [line.strip() for line in captured_output]
        self.assertEqual(captured_output_lines, expected_output)


if __name__ == "__main__":
    unittest.main()
