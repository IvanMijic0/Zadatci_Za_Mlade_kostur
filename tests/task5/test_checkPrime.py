import unittest

from tasks.task5.checkPrime import isPrime


class TestPrimeNumber(unittest.TestCase):
    def test_prime_number(self):
        self.assertFalse(isPrime(1))
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(3))
        self.assertFalse(isPrime(4))
        self.assertTrue(isPrime(5))
        self.assertFalse(isPrime(9))
        self.assertTrue(isPrime(13))


if __name__ == "__main__":
    unittest.main()
