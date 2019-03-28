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
   * [dynamic_array_implementation](algorithms/arrays/dynamic_array_implementation.py)
   * [number_plus_one](algorithms/arrays/number_plus_one.py)
   * [remove_duplicates_two](algorithms/arrays/remove_duplicates_two.py)
   * [merge_sorted_array](algorithms/arrays/merge_sorted_array.py)
   * [rotate_array](algorithms/arrays/rotate_array.py)
   * [contains_duplicate_one](algorithms/arrays/contains_duplicate_one.py)
 
 * [Backtracking](algorithms/backtracking)
   * [letter_combinations](algorithms/backtracking/letter_combinations.py)
   * [permutations_one](algorithms/backtracking/permutations_one.py)
   * [permutations_two](algorithms/backtracking/permutations_two.py)
   * [subsets](algorithms/backtracking/subsets.py)
   * [subsets_duplicates](algorithms/backtracking/subsets_duplicates.py)
   * [combinations_sum](algorithms/backtracking/combinations_sum.py)
   * [combinations_sum_two](algorithms/backtracking/combinations_sum_two.py)
   * [generate_paranthesis](algorithms/backtracking/generate_paranthesis.py)
 
 * [Binary Search](algorithms/binarysearch)
   * [search_insert_position](algorithms/binarysearch/search_insert_position.py)
   * [valid_perfect_square](algorithms/binarysearch/valid_perfect_square.py)
 
 * [Bits](algorithms/bits)
   * [single_number](algorithms/bits/single_number.py)
 
 * [Binary Search Tree](algorithms/bst)
   * [bst_implementation](algorithms/bst/bst_implementation.py)
   * [delete_node](algorithms/bst/delete_node.py)
   * [recover_bst](algorithms/bst/recover_bst.py)
   * [validate_bst](algorithms/bst/validate_bst.py)
 
 * [Dynamic Programming](algorithms/dp)
   * [climbing_stairs](algorithms/dp/climbing_stairs.py)
   * [fibonacci](algorithms/dp/fibonacci.py)
   * [kth_grammar](algorithms/dp/kth_grammar.py)
   * [pascal_row](algorithms/dp/pascal_row.py)
   * [pow](algorithms/dp/pow.py)
   * [pascal](algorithms/dp/pascal.py)
 
 * [Graphs](algorithms/graphs)
   * [graph_implementation](algorithms/graphs/graph_implementation.py)
   * [is_bipartate](algorithms/graphs/is_bipartate.py)
   * [surround_region](algorithms/graphs/surround_region.py)
   * [word_ladder_two](algorithms/graphs/word_ladder_two.py)
   * [word_ladder](algorithms/graphs/word_ladder.py)
   * [number_islands](algorithms/graphs/number_islands.py)
   * [clone_graph](algorithms/graphs/clone_graph.py)
   * [course_order](algorithms/graphs/course_order.py)
   * [bt_right_view](algorithms/graphs/bt_right_view.py)
 
 * [Hashtables](algorithms/hashtables)
   * [four_sum](algorithms/hashtables/four_sum.py)
   * [hashmap_implementation](algorithms/hashtables/hashmap_implementation.py)
   * [substring_concat](algorithms/hashtables/substring_concat.py)
   * [three_sum](algorithms/hashtables/three_sum.py)
   * [two_sum](algorithms/hashtables/two_sum.py)
   * [valid_sudoku](algorithms/hashtables/valid_sudoku.py)
 
 * [Heaps](algorithms/heaps)
   * [heap_implementation](algorithms/heaps/heap_implementation.py)
   * [k_most_frequent](algorithms/heaps/k_most_frequent.py)
   * [kth_largest](algorithms/heaps/kth_largest.py)
 
 * [Linkedlist](algorithms/linkedlist)
   * [add_two_numbers](algorithms/linkedlist/add_two_numbers.py)
   * [merge_k_lists](algorithms/linkedlist/merge_k_lists.py)
   * [merge_two_lists](algorithms/linkedlist/merge_two_lists.py)
   * [remove_nth_end](algorithms/linkedlist/remove_nth_end.py)
   * [reverse_k_groups](algorithms/linkedlist/reverse_k_groups.py)
   * [reverse_linkedlist](algorithms/linkedlist/reverse_linkedlist.py)
   * [reverse_mn](algorithms/linkedlist/reverse_mn.py)
   * [singly_linked_list](algorithms/linkedlist/singly_linked_list.py)
   * [swap_pairs](algorithms/linkedlist/swap_pairs.py)
   * [delete_duplicates](algorithms/linkedlist/delete_duplicates.py)
   * [linked_cycle](algorithms/linkedlist/linked_cycle.py)
   * [intersection](algorithms/linkedlist/intersection.py)
   * [remove_element](algorithms/linkedlist/remove_element.py)
   * [list_palindrome](algorithms/linkedlist/list_palindrome.py)
 
 * [Math](algorithms/math)
   * [add_binary](algorithms/math/add_binary.py)
   * [happy_numbers](algorithms/math/happy_numbers.py)
   * [count_primes](algorithms/math/count_primes.py)
   * [divide_two_numbers](algorithms/math/divide_two_numbers.py)
   * [num_to_col](algorithms/math/num_to_col.py)
   * [convert_to_number](algorithms/math/convert_to_number.py)
   * [majority_element](algorithms/math/majority_element.py)
 
 * [Matrix](algorithms/matrix)
   * [rotate_image](algorithms/matrix/rotate_image.py)
   * [spiral_matrix_generate](algorithms/matrix/spiral_matrix_generate.py)
   * [spiral_matrix](algorithms/matrix/spiral_matrix.py)
 
 * [Queues](algorithms/queues)
   * [queue_implementation](algorithms/queues/queue_implementation.py)
 
 * [Stack](algorithms/stack)
   * [valid_paran](algorithms/stack/valid_paran.py)
 
 * [Strings](algorithms/strings)
   * [add_binary](algorithms/strings/add_binary.py)
   * [count_say](algorithms/strings/count_say.py)
   * [int_to_roman](algorithms/strings/int_to_roman.py)
   * [length_of_last_word](algorithms/strings/length_of_last_word.py)
   * [longest_common_prefix](algorithms/strings/longest_common_prefix.py)
   * [longest_palin_substring](algorithms/strings/longest_palin_substring.py)
   * [longest_substring_without_repeating](algorithms/strings/longest_substring_without_repeating.py)
   * [multiply_strings](algorithms/strings/multiply_strings.py)
   * [palindrome](algorithms/strings/palindrome.py)
   * [reverse_int](algorithms/strings/reverse_int.py)
   * [reverse_string](algorithms/strings/reverse_string.py)
   * [roman_to_int](algorithms/strings/roman_to_int.py)
   * [string_to_integer](algorithms/strings/string_to_integer.py)
   * [strstr](algorithms/strings/strstr.py)
   * [zigzag_conversion](algorithms/strings/zigzag_conversion.py)
   * [permutations_in_string](algorithms/strings/permutations_in_string.py)
   * [jewels](algorithms/strings/jewels.py)
   * [to_lower](algorithms/strings/to_lower.py)
   * [valid_palin](algorithms/strings/valid_palin.py)
   * [isomorphic](algorithms/strings/isomorphic.py)
 
 * [Trees](algorithms/trees)
   * [average_levels](algorithms/trees/average_levels.py)
   * [build_tree_postorder](algorithms/trees/build_tree_postorder.py)
   * [construct_pre_in](algorithms/trees/construct_pre_in.py)
   * [inorder](algorithms/trees/inorder.py)
   * [invert_tree](algorithms/trees/invert_tree.py)
   * [largest_value_level](algorithms/trees/largest_value_level.py)
   * [level_order_one](algorithms/trees/level_order_one.py)
   * [level_order_two](algorithms/trees/level_order_two.py)
   * [max_depth](algorithms/trees/max_depth.py)
   * [min_depth](algorithms/trees/min_depth.py)
   * [postorder](algorithms/trees/postorder.py)
   * [preorder](algorithms/trees/preorder.py)
   * [same_tree](algorithms/trees/same_tree.py)
   * [symmetric](algorithms/trees/symmetric.py)
   * [tree_implementation](algorithms/trees/tree_implementation.py)
   * [zigzag_level_order](algorithms/trees/zigzag_level_order.py)
   * [array_bst](algorithms/trees/array_bst.py)
   * [is_balanced](algorithms/trees/is_balanced.py)
 
 * [Twopointers](algorithms/twopointers)
   * [remove_duplicates](algorithms/twopointers/remove_duplicates.py)
   * [remove_element](algorithms/twopointers/remove_element.py)
   * [three_sum_closest](algorithms/twopointers/three_sum_closest.py)









