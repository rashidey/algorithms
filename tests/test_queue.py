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

