Data Structures and Algorithms
==============================
 
This repository contains my implementations of data structures and algorithms using Python 3. Most of the algorithm questions are taken from LeetCode. This is a work in progress.

## Install
You can use this as an API in your code as follows:

	$ pip3 install algorithms3

An example of running an algorithm:

```python3
#Check if a string containing brackets is valid or not

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

## Progress
**Data Structures** : 8  
**Algorithms** &nbsp; &nbsp; &nbsp; &nbsp; : 101

## List of Implementations

* [Arrays](algorithms/arrays)
	* [Dynamic Array Implementation](algorithms/arrays/dynamic_array_implementation.py)
	* [Number plus one](algorithms/arrays/number_plus_one.py)
	* [Remove duplicates from array II](algorithms/arrays/remove_duplicates.py)
	* [Merge Sorted Array](algorithms/arrays/merge_sorted_array.py)
	* [Rotate Array](algorithms/arrays/rotate_array.py)
	* [Contains Duplicate I](algorithms/arrays/contains_duplicate_one.py)

* [Backtracking](algorithms/backtracking)
	* [Letter combinations of phone](algorithms/backtracking/letter_combinations.py)
	* [Permutations I](algorithms/backtracking/permutations_one.py)
	* [Permutations II](algorithms/backtracking/permutations_two.py)
	* [Subsets I](algorithms/backtracking/subsets.py)
	* [Subsets II](algorithms/backtracking/subsets_duplicates.py)
	* [Combinations Sum](algorithms/backtracking/combinations_sum.py)
	* [Combinations Sum II](algorithms/backtracking/combinations_sum_two.py)
	* [Generate Paranthesis](algorithms/backtracking/generate_paranthesis.py)

* [Binary Search](algorithms/binarysearch)
	* [Search Insert Position](algorithms/binarysearch/search_insert_position.py)
	* [Valid Perfect Square](algorithms/binarysearch/valid_perfect_square.py)

* [Binary Search Tree](algorithms/bst)
	* [Binary Search Tree Implementation](algorithms/bst/bst.py)
	* [Recover BST swapped nodes](algorithms/bst/recover_bst.py)
	* [Delete Node in BST](algorithms/bst/delete_node.py)
	* [Validate BST](algorithms/bst/validate_bst.py)


* [Dynamic Programming](algorithms/dp)
	* [Pascal's Triangle](algorithms/dp/pascal.py)
	* [Pascal's Triangle Row](algorithms/dp/pascal_row.py)
	* [Kth symbol in Grammar](algorithms/dp/kth_grammar.py)
	* [Implement power function](algorithms/dp/pow.py)
	* [Climbing stairs](algorithms/dp/climbing_stairs.py)
	* [Fibonacci](algorithms/dp/fibonacci.py)

* [Graphs](algorithms/graphs)
	* [Graph Implementation](algorithms/graphs/graph_implementation.py)
	* [Word Ladder](algorithms/graphs/word_ladder.py)
	* [Word Ladder II](algorithms/graphs/word_ladder_two.py)
	* [Number of Islands](algorithms/graphs/number_islands.py)
	* [Clone Graph](algorithms/graphs/clone_graph.py)
	* [Is Bipartite](algorithms/graphs/is_bipartate.py)
	* [Course Schedule](algorithms/graphs/course_order.py)
	* [BT Right Side View](algorithms/graphs/bt_right_view.py)


* [Hash Tables](algorithms/hashtables)
	* [Hash table implementation using linear probing](algorithms/hashtables/hashmap_implementation.py)
	* [Two Sum](algorithms/hashtables/two_sum.py)
	* [Three Sum](algorithms/hashtables/three_sum.py)
	* [Four Sum](algorithms/hashtables/four_sum.py)
	* [Substring with Concatenation of all words](algorithms/hashtables/substring_concat.py)
	* [Valid Sudoku](algorithms/hashtables/valid_sudoku.py)

* [Heaps](algorithms/heaps)
	* [Heap implementation](algorithms/heaps/heap_implementation.py)
	* [Kth Largest element](algorithms/heaps/kth_largest.py)
	* [Top k frequent elements](algorithms/heaps/k_most_frequent.py)

* [Linked List](algorithms/linkedlist)
	* [Singly Linked List implementation](algorithms/linkedlist/singly_linked_list.py)
	* [Add two numbers as Linked List](algorithms/linkedlist/add_two_numbers.py)
	* [Merge k lists](algorithms/linkedlist/merge_k_lists.py)
	* [Merge 2 lists](algorithms/linkedlist/merge_two_lists.py)
	* [Remove nth node from end](algorithms/linkedlist/remove_nth_end.py)
	* [Swap Nodes in Pairs](algorithms/linkedlist/swap_pairs.py)
	* [Reverse Nodes in k Groups](algorithms/linkedlist/reverse_k_groups.py)
	* [Reverse a linked list](algorithms/linkedlist/reverse_linkedlist.py)
	* [Reverse a linked list II](algorithms/linkedlist/reverse_mn.py)
	* [LinkedList Cycle](algorithms/linkedlist/linked_cycle.py)
	* [Delete Duplicates](algorithms/linkedlist/delete_duplicates.py)
	* [Linked List palindrome](algorithms/linkedlist/list_palindrome.py)
	* [Remove List elements](algorithms/linkedlist/remove_element.py)
	* [Intersection Lists](algorithms/linkedlist/intersection.py)


* [Math](algorithms/math)
	* [Add two binary numbers](algorithms/math/add_binary.py)
	* [Count Primes](algorithms/math/count_primes.py)
	* [Divide Two numbers](algorithms/math/divide_two_numbers.py)
	* [Happy Numbers](algorithms/math/happy_numbers.py)
	* [Majority Element](algorithms/math/majority_element.py)
	* [Excel Column to Number](algorithms/math/convert_to_number.py)
	* [Excel Number to Column](algorithms/math/num_to_col.py)


* [Matrix](algorithms/matrix)
	* [Rotate Image](algorithms/matrix/rotate_image.py)
	* [Spiral Matrix](algorithms/matrix/spiral_matrix.py)
	* [Generate Spiral Matrix](algorithms/matrix/spiral_matrix_generate.py)

* [Queues](algorithms/queues)
 	* [Queue implementation using Linked List](algorithms/queues/queue_implementation.py)

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
	* [Multiply Strings](algorithms/strings/multiply_strings.py)
	* [Reverse a string](algorithms/strings/reverse_string.py)
	* [Permutations in string](algorithms/strings/permutations_in_string.py)
	* [Jewels and stones](algorithms/strings/jewels.py)
	* [To lower case](algorithms/strings/to_lower.py)
	* [Valid Palindrome](algorithms/strings/valid_palin.py)
	* [Isomorphic Strings](algorithms/strings/isomorphic.py)
	

* [Trees](algorithms/trees)
	* [Binary Tree Implementation](algorithms/trees/tree_implementation.py)
	* [Inorder Traversal](algorithms/trees/inorder.py)
	* [Postorder Traversal](algorithms/trees/postorder.py)
	* [Preorder Traversal](algorithms/trees/preorder.py)
	* [Level order traversal I](algorithms/trees/level_order_one.py)
	* [Level order traversal II](algorithms/trees/level_order_two.py)
	* [ZigZag Level order traversal](algorithms/trees/zigzag_level_order.py)
	* [Build tree from postorder, inorder](algorithms/trees/build_tree_postorder.py)
	* [Build tree from inorder, preorder](algorithms/trees/construct_pre_in.py)
	* [Max Depth Tree](algorithms/trees/max_depth.py)
	* [Min Depth Tree](algorithms/trees/min_depth.py)
	* [Same Tree](algorithms/trees/same_tree.py)
	* [Symmetric Tree](algorithms/trees/symmetric.py)
	* [Largest Value in level order](algorithms/trees/largest_value_level.py)
	* [Average Value in level order](algorithms/trees/average_levels.py)
	* [Invert tree](algorithms/trees/invert_tree.py)
	* [Array to BST](algorithms/trees/array_bst.py)
	* [Balanced Tree](algorithms/trees/is_balanced.py)

* [Two Pointers](algorithms/twopointers)
	* [Remove Duplicates](algorithms/twopointers/remove_duplicates.py)
	* [Remove element](algorithms/twopointers/remove_element.py)
	* [Three Sum closest](algorithms/twopointers/three_sum_closest.py)

