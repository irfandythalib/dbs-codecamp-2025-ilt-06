import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 3), 13)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

class TestSubtractionOperations(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()