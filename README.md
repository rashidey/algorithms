Data Structures and Algorithms
==============================
 
This repository contains my implementations of data structures and algorithms using Python 3. Most of the algorithm questions are taken from LeetCode. This is a work in progress.

## Install
You can use this as an API in your code as follows:

	$ pip3 install algorithms3

An example of running an algorithm:

```python3
#Check if a string containing brackets is valid or not
#Returns bool value

from algorithms.stack import is_valid

if __name__ == '__main__':
	test = is_valid('()[]')
	print(test)
```

If an algorithm is listed in this repository but is not in the pip package, it means that I have not uploaded the latest version. I will be doing that once a week. 

## Uninstall
If you want to uninstall, simply run:

	$pip3 uninstall algorithms3

## Tests
I have written basic tests for most of the modules. To run all the tests at once run:
	
	$python3 -m unittest discover tests

## List of Implementations

* [Arrays](algorithms/arrays)
	* [Number plus one](algorithms/arrays/number_plus_one.py)

* [Backtracking](algorithms/backtracking)
	* [Letter combinations of phone](algorithms/backtracking/letter_combinations.py)

* [Binary Search](algorithms/binarysearch)
	* [Search Insert Position](algorithms/binarysearch/search_insert_position.py)

* [Binary Search Tree](algorithms/bst)
	* [Binary Search Tree Implementation](algorithms/bst/bst.py)
	* [Recover BST swapped nodes](algorithms/bst/recover_bst.py)

* [Hash Tables](algorithms/hashtables)
	* [Two Sum](algorithms/hashtables/two_sum.py)
	* [Three Sum](algorithms/hashtables/three_sum.py)
	* [Four Sum](algorithms/hashtables/four_sum.py)
	* [Substring with Concatenation of all words](algorithms/hashtables/substring_concat.py)

* [Heaps](algorithms/heaps)
	* [Kth Largest element](algorithms/heaps/kth_largest.py)

* [Linked List](algorithms/linkedlist)
	* [Singly Linked List implementation](algorithms/linkedlist/singly_linked_list.py)
	* [Add two numbers as Linked List](algorithms/linkedlist/add_two_numbers.py)
	* [Merge k lists](algorithms/linkedlist/merge_k_lists.py)
	* [Merge 2 lists](algorithms/linkedlist/merge_two_lists.py)
	* [Remove nth node from end](algorithms/linkedlist/remove_nth_end.py)
	* [Swap Nodes in Pairs](algorithms/linkedlist/swap_pairs.py)
	* [Reverse Nodes in k Groups](algorithms/linkedlist/reverse_k_groups.py)

* [Stack](algorithms/stack)
	* [Check Valid Paranthesis](algorithms/stack/valid_paran.py)

* [Strings](algorithms/strings)
	* [Integer to Roman](algorithms/strings/int_to_roman.py)
	* [Roman to Integer](algorithms/strings/roman_to_int.py)
	* [Check integer Palindrome](algorithms/strings/palindrome.py)
	* [Reverse Integer](algorithms/strings/reverse_int.py)
	* [Longest Common Prefix](algorithms/strings/longest_common_prefix.py)
	* [strstr implementation](algorithms/strings/strstr.py)
	* [Longest Palindromic String](algorithms/strings/longest_palin_substring.py)
	* [String to Integer](algorithms/strings/string_to_integer.py)
	* [Longest Substring Without repitition](algorithms/strings/longest_substring_without_repeating.py)
	* [Zig zag conversion string](algorithms/strings/zigzag_conversion.py)
	* [Length of last Word](algorithms/strings/length_of_last_word.py)
	* [Count and Say](algorithms/strings/count_say.py)


* [Two Pointers](algorithms/twopointers)
	* [Remove Duplicates](algorithms/twopointers/remove_duplicates.py)
	* [Remove element](algorithms/twopointers/remove_element.py)


