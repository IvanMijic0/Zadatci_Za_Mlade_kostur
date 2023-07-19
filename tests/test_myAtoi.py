import unittest

from tasks.task1.myAtoi import myAtoi


class TestMyAtoi(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(myAtoi(""), 0)

    def test_whitespace_string(self):
        self.assertEqual(myAtoi("   "), 0)

    def test_positive_number(self):
        self.assertEqual(myAtoi("42"), 42)

    def test_negative_number(self):
        self.assertEqual(myAtoi("-42"), -42)

    def test_positive_number_with_plus_sign(self):
        self.assertEqual(myAtoi("+42"), 42)

    def test_leading_whitespace(self):
        self.assertEqual(myAtoi("   -42"), -42)

    def test_trailing_characters(self):
        self.assertEqual(myAtoi("4193 with words"), 4193)

    def test_invalid_input(self):
        self.assertEqual(myAtoi("words and 987"), 0)

    def test_integer_out_of_range(self):
        self.assertEqual(myAtoi("-91283472332"), -2147483648)


if __name__ == "__main__":
    unittest.main()
