from algorithms.dp import *
import unittest

class TestSuite(unittest.TestCase):
    def test_pascal(self):
        self.assertEqual(pascal(1), [[1]])
        self.assertEqual(pascal(2), [[1], [1,1]])
        self.assertEqual(pascal(3), [[1], [1,1], [1,2,1]])
        self.assertEqual(pascal(4), [[1], [1,1], [1,2,1],[1,3,3,1]])

    def test_pascal_row(self):
        self.assertEqual(pascal_row(1), [1])
        self.assertEqual(pascal_row(2), [1,1])
        self.assertEqual(pascal_row(3), [1,2,1])
        self.assertEqual(pascal_row(4), [1,3,3,1])

    def test_fibonacci(self):
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_dynamic(1), 1)
        self.assertEqual(fibonacci_dynamic_v2(1), 1)
        self.assertEqual(fibonacci_formula(10), 89)

    def test_climb_stairs(self):
        self.assertEqual(climbing_stairs(3), 3)

    def test_power(self):
        self.assertEqual(pow_v3(2,3), 8)
        self.assertEqual(pow_v3(2,-3), 0.125)