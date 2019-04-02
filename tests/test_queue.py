from algorithms.queues import *
import unittest

class TestSuite(unittest.TestCase):
    def test_queue_implementation(self):
        q1 = Queue()
        q1.enque(1)
        q1.enque(2)
        q1.enque(3)
        self.assertEqual(q1.deque(), 1)
        self.assertEqual(q1.deque(), 2)
        self.assertEqual(q1.deque(), 3)
        self.assertEqual(q1.deque(), None)
        self.assertEqual(q1.is_empty(), True)
        q1.enque(3)
        self.assertEqual(q1.front_que(), 3)

    def test_my_stack(self):
        test = MyStack()
        test.push(1)
        test.push(2)
        self.assertEqual(test.top(), 2)
        self.assertEqual(test.pop(), 2)
        self.assertEqual(test.empty(), False)

    def test_gas_station(self):
        self.assertEqual(route_possible([1,2,3,4,5], [3,4,5,1,2]), 3)
        self.assertEqual(route_possible([2,3,4], [3,4,3]), -1)