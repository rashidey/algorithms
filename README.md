
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
**Algorithms** &nbsp; &nbsp; &nbsp; &nbsp; : 120

## List of Implementations



* [**Arrays**](/algorithms/arrays)  
    - [*Dynamic Array Implementation*](/algorithms/arrays/dynamic_array_implementation.py)  
    - [Contains Duplicate One](/algorithms/arrays/contains_duplicate_one.py)  
    - [Merge Intervals](/algorithms/arrays/merge_intervals.py)  
    - [Merge Sorted Array](/algorithms/arrays/merge_sorted_array.py)  
    - [Number Plus One](/algorithms/arrays/number_plus_one.py)  
    - [Remove Duplicates Two](/algorithms/arrays/remove_duplicates_two.py)  
    - [Rotate Array](/algorithms/arrays/rotate_array.py)  
* [**Backtracking**](/algorithms/backtracking)  
    - [Combinations Sum Two](/algorithms/backtracking/combinations_sum_two.py)  
    - [Combinations Sum](/algorithms/backtracking/combinations_sum.py)  
    - [Generate Paranthesis](/algorithms/backtracking/generate_paranthesis.py)  
    - [Letter Combinations](/algorithms/backtracking/letter_combinations.py)  
    - [Permutations One](/algorithms/backtracking/permutations_one.py)  
    - [Permutations Two](/algorithms/backtracking/permutations_two.py)  
    - [Subsets Duplicates](/algorithms/backtracking/subsets_duplicates.py)  
    - [Subsets](/algorithms/backtracking/subsets.py)  
* [**Binarysearch**](/algorithms/binarysearch)  
    - [Binary Search](/algorithms/binarysearch/binary_search.py)  
    - [Find Peak](/algorithms/binarysearch/find_peak.py)  
    - [First Bad](/algorithms/binarysearch/first_bad.py)  
    - [Guess Number](/algorithms/binarysearch/guess_number.py)  
    - [Search Insert Position](/algorithms/binarysearch/search_insert_position.py)  
    - [Search Range](/algorithms/binarysearch/search_range.py)  
    - [Search Rotated Array](/algorithms/binarysearch/search_rotated_array.py)  
    - [Sqrt Number](/algorithms/binarysearch/sqrt_number.py)  
    - [Valid Perfect Square](/algorithms/binarysearch/valid_perfect_square.py)  
* [**Bits**](/algorithms/bits)  
    - [Single Number](/algorithms/bits/single_number.py)  
* [**Binary Search Tree**](/algorithms/bst)  
    - [*Bst Implementation*](/algorithms/bst/bst_implementation.py)  
    - [Delete Node](/algorithms/bst/delete_node.py)  
    - [Recover Bst](/algorithms/bst/recover_bst.py)  
    - [Validate Bst](/algorithms/bst/validate_bst.py)  
* [**Dynamic Programming**](/algorithms/dp)  
    - [Climbing Stairs](/algorithms/dp/climbing_stairs.py)  
    - [Fibonacci](/algorithms/dp/fibonacci.py)  
    - [Kth Grammar](/algorithms/dp/kth_grammar.py)  
    - [Pascal Row](/algorithms/dp/pascal_row.py)  
    - [Pascal](/algorithms/dp/pascal.py)  
    - [Pow](/algorithms/dp/pow.py)  
* [**Graphs**](/algorithms/graphs)  
    - [*Graph Implementation*](/algorithms/graphs/graph_implementation.py)  
    - [Bt Right View](/algorithms/graphs/bt_right_view.py)  
    - [Clone Graph](/algorithms/graphs/clone_graph.py)  
    - [Course Order](/algorithms/graphs/course_order.py)  
    - [Is Bipartate](/algorithms/graphs/is_bipartate.py)  
    - [Number Islands](/algorithms/graphs/number_islands.py)  
    - [Surround Region](/algorithms/graphs/surround_region.py)  
    - [Word Ladder Two](/algorithms/graphs/word_ladder_two.py)  
    - [Word Ladder](/algorithms/graphs/word_ladder.py)  
* [**Hash Tables**](/algorithms/hashtables)  
    - [*Hashmap Implementation*](/algorithms/hashtables/hashmap_implementation.py)  
    - [Four Sum](/algorithms/hashtables/four_sum.py)  
    - [Group Anagrams](/algorithms/hashtables/group_anagrams.py)  
    - [Substring Concat](/algorithms/hashtables/substring_concat.py)  
    - [Three Sum](/algorithms/hashtables/three_sum.py)  
    - [Two Sum](/algorithms/hashtables/two_sum.py)  
    - [Valid Sudoku](/algorithms/hashtables/valid_sudoku.py)  
* [**Heaps**](/algorithms/heaps)  
    - [*Heap Implementation*](/algorithms/heaps/heap_implementation.py)  
    - [K Most Frequent](/algorithms/heaps/k_most_frequent.py)  
    - [Kth Largest](/algorithms/heaps/kth_largest.py)  
* [**Linked List**](/algorithms/linkedlist)  
    - [*Singly Linked List Implementation*](/algorithms/linkedlist/singly_linked_list_implementation.py)  
    - [Add Two Numbers](/algorithms/linkedlist/add_two_numbers.py)  
    - [Delete Duplicates](/algorithms/linkedlist/delete_duplicates.py)  
    - [Intersection](/algorithms/linkedlist/intersection.py)  
    - [Linked Cycle](/algorithms/linkedlist/linked_cycle.py)  
    - [List Palindrome](/algorithms/linkedlist/list_palindrome.py)  
    - [Merge K Lists](/algorithms/linkedlist/merge_k_lists.py)  
    - [Merge Two Lists](/algorithms/linkedlist/merge_two_lists.py)  
    - [Remove Element](/algorithms/linkedlist/remove_element.py)  
    - [Remove Nth End](/algorithms/linkedlist/remove_nth_end.py)  
    - [Reverse K Groups](/algorithms/linkedlist/reverse_k_groups.py)  
    - [Reverse Linkedlist](/algorithms/linkedlist/reverse_linkedlist.py)  
    - [Reverse Mn](/algorithms/linkedlist/reverse_mn.py)  
    - [Swap Pairs](/algorithms/linkedlist/swap_pairs.py)  
* [**Math**](/algorithms/math)  
    - [Add Binary](/algorithms/math/add_binary.py)  
    - [Convert To Number](/algorithms/math/convert_to_number.py)  
    - [Count Primes](/algorithms/math/count_primes.py)  
    - [Divide Two Numbers](/algorithms/math/divide_two_numbers.py)  
    - [Happy Numbers](/algorithms/math/happy_numbers.py)  
    - [Majority Element](/algorithms/math/majority_element.py)  
    - [Next Permutation](/algorithms/math/next_permutation.py)  
    - [Num To Col](/algorithms/math/num_to_col.py)  
* [**Matrix**](/algorithms/matrix)  
    - [Rotate Image](/algorithms/matrix/rotate_image.py)  
    - [Spiral Matrix Generate](/algorithms/matrix/spiral_matrix_generate.py)  
    - [Spiral Matrix](/algorithms/matrix/spiral_matrix.py)  
* [**Queues**](/algorithms/queues)  
    - [*Queue Implementation*](/algorithms/queues/queue_implementation.py)  
* [**Stack**](/algorithms/stack)  
    - [Valid Paran](/algorithms/stack/valid_paran.py)  
* [**Strings**](/algorithms/strings)  
    - [Add Binary](/algorithms/strings/add_binary.py)  
    - [Count Say](/algorithms/strings/count_say.py)  
    - [Int To Roman](/algorithms/strings/int_to_roman.py)  
    - [Isomorphic](/algorithms/strings/isomorphic.py)  
    - [Jewels](/algorithms/strings/jewels.py)  
    - [Length Of Last Word](/algorithms/strings/length_of_last_word.py)  
    - [Longest Common Prefix](/algorithms/strings/longest_common_prefix.py)  
    - [Longest Palin Substring](/algorithms/strings/longest_palin_substring.py)  
    - [Longest Substring Without Repeating](/algorithms/strings/longest_substring_without_repeating.py)  
    - [Multiply Strings](/algorithms/strings/multiply_strings.py)  
    - [Palindrome](/algorithms/strings/palindrome.py)  
    - [Permutations In String](/algorithms/strings/permutations_in_string.py)  
    - [Reverse Int](/algorithms/strings/reverse_int.py)  
    - [Reverse String](/algorithms/strings/reverse_string.py)  
    - [Roman To Int](/algorithms/strings/roman_to_int.py)  
    - [String To Integer](/algorithms/strings/string_to_integer.py)  
    - [Strstr](/algorithms/strings/strstr.py)  
    - [To Lower](/algorithms/strings/to_lower.py)  
    - [Valid Palin](/algorithms/strings/valid_palin.py)  
    - [Zigzag Conversion](/algorithms/strings/zigzag_conversion.py)  
* [**Trees**](/algorithms/trees)  
    - [*Tree Implementation*](/algorithms/trees/tree_implementation.py)  
    - [Array Bst](/algorithms/trees/array_bst.py)  
    - [Average Levels](/algorithms/trees/average_levels.py)  
    - [Build Tree Postorder](/algorithms/trees/build_tree_postorder.py)  
    - [Construct Pre In](/algorithms/trees/construct_pre_in.py)  
    - [Inorder](/algorithms/trees/inorder.py)  
    - [Invert Tree](/algorithms/trees/invert_tree.py)  
    - [Is Balanced](/algorithms/trees/is_balanced.py)  
    - [Largest Value Level](/algorithms/trees/largest_value_level.py)  
    - [Level Order One](/algorithms/trees/level_order_one.py)  
    - [Level Order Two](/algorithms/trees/level_order_two.py)  
    - [Max Depth](/algorithms/trees/max_depth.py)  
    - [Merge Two Trees](/algorithms/trees/merge_two_trees.py)  
    - [Min Depth](/algorithms/trees/min_depth.py)  
    - [Path Sum All](/algorithms/trees/path_sum_all.py)  
    - [Path Sum](/algorithms/trees/path_sum.py)  
    - [Postorder](/algorithms/trees/postorder.py)  
    - [Preorder](/algorithms/trees/preorder.py)  
    - [Same Tree](/algorithms/trees/same_tree.py)  
    - [Sum Root To Leaf Paths](/algorithms/trees/sum_root_to_leaf_paths.py)  
    - [Symmetric](/algorithms/trees/symmetric.py)  
    - [Tree Paths](/algorithms/trees/tree_paths.py)  
    - [Zigzag Level Order](/algorithms/trees/zigzag_level_order.py)  
* [**Two Pointers**](/algorithms/twopointers)  
    - [Container With Most Water](/algorithms/twopointers/container_with_most_water.py)  
    - [Remove Duplicates](/algorithms/twopointers/remove_duplicates.py)  
    - [Remove Element](/algorithms/twopointers/remove_element.py)  
    - [Three Sum Closest](/algorithms/twopointers/three_sum_closest.py)  
