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

    def test_rpn(self):
        self.assertEqual(eval_rpn(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(eval_rpn(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(eval_rpn(["10", "6", "9", "3", "+", "-11", 
                                   "*", "/", "*", "17", "+", "5", "+"]), 22)

    def test_baseball(self):
        self.assertEqual(baseball(["5","-2","4","C","D","9","+","+"]), 27)

if __name__ == '__main__':
    unittest.main()