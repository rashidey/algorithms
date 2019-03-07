from algorithms.linkedlist import *

import unittest

def convert_to_list(A):
    dummy = newList = Node(0)
    for number in A:
        dummy.next = Node(number)
        dummy = dummy.next
    return newList.next


def print_list(A):
    result = ''
    while A:
        result += str(A.val)
        A = A.next
    return result

class TestSetup(unittest.TestCase):
    def setUp(self):
        self.l1 = SinglyLinkedList()
        self.l2 = SinglyLinkedList()
        self.l3 = SinglyLinkedList()
        self.l4 = SinglyLinkedList()
        self.l5 = SinglyLinkedList()

        self.l2.head = Node(1)

        self.l3.head = Node(1)
        self.l3.head.next = Node(2)

        self.l4.head = Node(1)
        self.l4.head.next = Node(2)
        self.l4.head.next.next = Node(3)

        self.l5.head = Node(1)
        self.l5.head.next = Node(2)
        self.l5.head.next.next = Node(3)
        self.l5.head.next.next.next = Node(4)

class TestLinkedListBase(TestSetup):
    def test_repr(self):
        self.assertEqual('', str(self.l1))
        self.assertEqual('1', str(self.l2))
        self.assertEqual('1->2', str(self.l3))
        self.assertEqual('1->2->3', str(self.l4))
        self.assertEqual('1->2->3->4', str(self.l5))

    def test_len(self):
        self.assertEqual(0, len(self.l1))
        self.assertEqual(1, len(self.l2))
        self.assertEqual(2, len(self.l3))
        self.assertEqual(3, len(self.l4))
        self.assertEqual(4, len(self.l5))

    def test_push_front(self):
        self.l1.push_front(1)
        self.assertEqual('1', str(self.l1))
    
    def test_push_end(self):
        self.l1.push_end(2)
        self.assertEqual('2', str(self.l1))

class TestSLLFunctions(TestSetup):
    def test_add_two_numbers(self):
        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(3)
        head1 = Node(5)
        head1.next = Node(6)
        head1.next.next = Node(4)
        self.assertEqual('708', print_list(add_two_numbers(head, head1)))
        answer = add_two_numbers(convert_to_list([1,2]), convert_to_list([2,3,4]))
        self.assertEqual('354', print_list(answer))

    def test_mergeKLists(self):
        list1 = []
        list1.append(convert_to_list([1,4,5]))
        list1.append(convert_to_list([1,3,4]))
        list1.append(convert_to_list([2,6]))
        self.assertEqual('11234456', print_list(mergeKLists(list1)))

    def test_mergeTwoLists(self):
        list1 = convert_to_list([1,2,4])
        list2 = convert_to_list([1,3,4])
        self.assertEqual('112344', print_list(mergeTwoLists(list1, list2)))

    def test_removeNthFromEnd(self):
        list1 = convert_to_list([1,2,3,4,5])
        list2 = convert_to_list([])
        list3 = convert_to_list([1,2])
        self.assertEqual('1234', print_list(removeNthFromEnd(list1, 1)))
        self.assertEqual('124', print_list(removeNthFromEnd(list1, 2)))
        #self.assertEqual('1234', print_list(removeNthFromEnd(list2, 0)))
        self.assertEqual('1', print_list(removeNthFromEnd(list3, 1)))
        self.assertEqual('12', print_list(removeNthFromEnd(list1, 1)))
        self.assertEqual('2', print_list(removeNthFromEnd(list1, 2)))
        #self.assertEqual('', print_list(removeNthFromEnd(list1, 1)))



if __name__ == '__main__':
    unittest.main()

