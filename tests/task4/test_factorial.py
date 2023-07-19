import unittest

from tasks.task4.factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(15), 1307674368000)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            factorial(-5)


if __name__ == "__main__":
    unittest.main()
