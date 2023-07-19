import unittest
from tasks.task3.anagram import isAnagram


class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(isAnagram("anagram", "nagaram"))
        self.assertFalse(isAnagram("rat", "car"))
        self.assertTrue(isAnagram("listen", "silent"))
        self.assertFalse(isAnagram("hello", "world"))
        self.assertTrue(isAnagram("debit card", "bad credit"))