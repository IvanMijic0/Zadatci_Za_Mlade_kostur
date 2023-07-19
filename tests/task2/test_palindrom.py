import unittest
from tasks.task2.palindrom import isPalindrome


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(isPalindrome("race a car"))
        self.assertTrue(isPalindrome("Was it a car or a cat I saw?"))
        self.assertFalse(isPalindrome("Hello World"))
        self.assertFalse(isPalindrome("Python"))


if __name__ == "__main__":
    unittest.main()
