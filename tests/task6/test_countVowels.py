import unittest
from tasks.task6.countVowels import countVowels


class TestVowelCount(unittest.TestCase):
    def test_vowel_count(self):
        self.assertEqual(countVowels("Hello World"), 3)
        self.assertEqual(countVowels("Python Programming"), 4)
        self.assertEqual(countVowels("The quick brown fox jumps over the lazy dog"), 11)
        self.assertEqual(countVowels("OpenAI GPT-3"), 4)
        self.assertEqual(countVowels(""), 0)


if __name__ == "__main__":
    unittest.main()
