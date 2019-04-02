from algorithms.stack import *
import unittest

class TestSuite(unittest.TestCase):
    def test_is_valid(self):
        self.assertEqual(True, is_valid('()'))
        self.assertEqual(True, is_valid('()[]{}'))
        self.assertEqual(False, is_valid('(]'))
        self.assertEqual(False, is_valid('([)]'))
        self.assertEqual(True, is_valid('{[]}'))

    def test_simplify_path(self):
        self.assertEqual(simplify_path('/home/'), '/home')
        self.assertEqual(simplify_path("/../"), '/')
        self.assertEqual(simplify_path("/home//foo/"), '/home/foo')
        self.assertEqual(simplify_path("/a/./b/../../c/"), '/c')
        self.assertEqual(simplify_path('/a/../../b/../c//.//'), '/c')
        self.assertEqual(simplify_path('/a//b////c/d//././/..'), '/a/b/c')

    def test_min_stack(self):
        test = MinStack()
        test.push(1)
        test.push(2)
        minx = test.getMin()
        self.assertEqual(minx, 1)
        self.assertEqual(test.top(), 2)

if __name__ == '__main__':
    unittest.main()