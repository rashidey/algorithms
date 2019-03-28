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

    def test_is_empty(self):
        l1 = SinglyLinkedList()
        l1.push_end(1)
        l1.push_end(2)
        self.assertEqual(False, l1.is_empty())
        l1.pop_back()
        l1.pop_front()
        self.assertEqual(True, l1.is_empty())
        l1.push_end(1)
        l1.push_front(2)
        self.assertEqual(False, l1.is_empty())
        self.assertEqual(False, l1.is_empty())

    def test_pop_front(self):
        self.assertEqual(1, self.l2.pop_front())
        self.assertEqual(None, self.l1.pop_front())
        self.assertEqual(1, self.l5.pop_front())

    def test_pop_back(self):
        self.assertEqual(1, self.l2.pop_back())
        self.assertEqual(4, self.l5.pop_back())

    def test_get_item(self):
        self.assertEqual(3, self.l4[2])
        self.assertEqual(None, self.l4[12])

    def test_front_list(self):
        self.assertEqual(None, self.l1.front_list())
        self.assertEqual(1, self.l2.front_list())

    def test_back_list(self):
        self.assertEqual(None, self.l1.back_list())
        self.assertEqual(3, self.l4.back_list())

    def test_insert_list(self):
        l1 = SinglyLinkedList()
        l1.push_end(1)
        l1.push_end(2)
        l1.push_end(3)
        self.assertEqual('1->2->3', str(l1))
        l1.insert_list(0, 5)
        self.assertEqual('5->1->2->3', str(l1))
        l1.pop_front()
        l1.pop_front()
        l1.pop_front()
        l1.pop_front()
        l1.insert_list(0, 1)
        self.assertEqual('1', str(l1))
        l1.insert_list(1, 2)
        self.assertEqual('1->2', str(l1))
        l1.insert_list(1, 3)
        self.assertEqual('1->3->2', str(l1))

    def test_erase_list(self):
        l1 = SinglyLinkedList()
        l1.push_end(1)
        l1.push_end(2)
        l1.push_end(3)
        l1.head = l1.erase_list(2)
        self.assertEqual(str(l1), '1->2')
        l1.head = l1.erase_list(0)
        self.assertEqual(str(l1), '2')
        l1.head = l1.erase_list(1)
        self.assertEqual(str(l1), '2')
        l1.head = l1.erase_list(0)
        self.assertEqual(str(l1), '')

    def test_remove_value(self):
        l1 = SinglyLinkedList()
        l1.push_end(1)
        l1.push_end(2)
        l1.push_end(3)
        l1.head = l1.remove_value(1)
        self.assertEqual(str(l1), '2->3')
        l1.head = l1.remove_value(3)
        self.assertEqual(str(l1), '2')
        l1.head = l1.remove_value(2)
        self.assertEqual(str(l1), '')
        l1.push_end(1)
        l1.push_end(2)
        l1.push_end(3)
        l1.head = l1.remove_value(2)
        self.assertEqual(str(l1), '1->3')

    def test_reverse_list(self):
        l1 = SinglyLinkedList()
        l1.push_end(1)
        l1.push_end(2)
        l1.push_end(3)
        l1.head = l1.reverse_list()
        self.assertEqual(str(l1), '3->2->1')

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

    def test_merge_k_lists(self):
        list1 = []
        list1.append(convert_to_list([1,4,5]))
        list1.append(convert_to_list([1,3,4]))
        list1.append(convert_to_list([2,6]))
        self.assertEqual('11234456', print_list(merge_k_lists(list1)))

    def test_merge_two_lists(self):
        list1 = convert_to_list([1,2,4])
        list2 = convert_to_list([1,3,4])
        self.assertEqual('112344', print_list(merge_two_lists(list1, list2)))

    def test_remove_nth_end(self):
        list1 = convert_to_list([1,2,3,4,5])
        list2 = convert_to_list([])
        list3 = convert_to_list([1,2])
        self.assertEqual('1234', print_list(remove_nth_end(list1, 1)))
        self.assertEqual('124', print_list(remove_nth_end(list1, 2)))
        #self.assertEqual('1234', print_list(remove_nth_end(list2, 0)))
        self.assertEqual('1', print_list(remove_nth_end(list3, 1)))
        self.assertEqual('12', print_list(remove_nth_end(list1, 1)))
        self.assertEqual('2', print_list(remove_nth_end(list1, 2)))
        #self.assertEqual('', print_list(remove_nth_end(list1, 1)))

    def test_swap_pairs(self):
        list1 = convert_to_list([1,2,3,4])
        self.assertEqual('2143', print_list(swap_pairs(list1)))
        list2 = convert_to_list([1,2,3,4])
        self.assertEqual('2143', print_list(swap_pairs_v2(list2)))

    def test_reverse_k_group(self):
        list1 = convert_to_list([1,2,3,4,5])
        list2 = convert_to_list([1,2,3,4,5])

        self.assertEqual('21435', print_list(reverse_k_group(list1, 2)))
        self.assertEqual('32145', print_list(reverse_k_group(list2, 3)))

    def test_reverse_list_recursive(self):
        list1 = convert_to_list([1,2,3,4,5])
        list2 = convert_to_list([1,2,3,4,5])
        self.assertEqual(print_list(reverse_list_recursive(list1)), '54321')
        self.assertEqual(print_list(reverse_list_v2(list2)), '54321')

    def test_reverse_mn(self):
        list1 = convert_to_list([1,2,3,4,5])
        self.assertEqual(print_list(reverse_mn(list1, 2, 4)), '14325')

    def test_delete_duplicates(self):
        list1 = convert_to_list([1,1,2,3,3])
        self.assertEqual(print_list(delete_duplicates(list1)), '123')

    def test_has_cycle(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = head
        self.assertEqual(has_cycle(head), True)

    def test_intersection(self):
        head1 = Node(1)
        head1.next = Node(2)
        head1.next.next = Node(3)

        head2 = Node(4)
        head2.next = head1.next

        self.assertEqual(get_intersection(head1, head2), head1.next)

    def test_remove_elements(self):
        list1 = convert_to_list([1,2,6,3,4,5,6])
        self.assertEqual(print_list(remove_elements(list1, 6)), '12345')

    def test_list_palindrome(self):
        list1 = convert_to_list([1,2,3,4,3,2,1])
        list2 = convert_to_list([1,2,3,4,4,3,2,1])
        list3 = convert_to_list([1,2,1,2])
        list4 = convert_to_list([1,1,2,1])
        self.assertEqual(list_palindrome(list1), True)
        self.assertEqual(list_palindrome(list2), True)
        self.assertEqual(list_palindrome(list3), False)
        self.assertEqual(list_palindrome(list4), False)


if __name__ == '__main__':
    unittest.main()

