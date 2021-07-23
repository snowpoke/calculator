import unittest
from calculator import add

class TestMethods(unittest.TestCase):
    def test_math(self):
        self.assertEqual(add("4","6"), 10)
        self.assertEqual(add("-5","4"), -1)

if __name__ == "__main__":
    unittest.main()
