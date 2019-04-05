
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
**Data Structures** : 10  
**Algorithms** &nbsp; &nbsp; &nbsp; &nbsp; : 186

## List of Implementations



* [**Arrays**](/algorithms/arrays)  
    - [*Dynamic Array Implementation*](/algorithms/arrays/dynamic_array_implementation.py)  
    - [Best Time To Buy Stock Ii](/algorithms/arrays/best_time_to_buy_stock_II.py)  
    - [Best Time To Buy Stock](/algorithms/arrays/best_time_to_buy_stock.py)  
    - [Contains Duplicate One](/algorithms/arrays/contains_duplicate_one.py)  
    - [Contains Duplicate Range](/algorithms/arrays/contains_duplicate_range.py)  
    - [Find All Dissapeared Numbers](/algorithms/arrays/find_all_dissapeared_numbers.py)  
    - [Intersection Two Arrays Ii](/algorithms/arrays/intersection_two_arrays_II.py)  
    - [K Diff Pairs](/algorithms/arrays/k_diff_pairs.py)  
    - [Max Average Subarray](/algorithms/arrays/max_average_subarray.py)  
    - [Max Consecutive Ones](/algorithms/arrays/max_consecutive_ones.py)  
    - [Max Product Three Numbers](/algorithms/arrays/max_product_three_numbers.py)  
    - [Maximum Subarray](/algorithms/arrays/maximum_subarray.py)  
    - [Merge Intervals](/algorithms/arrays/merge_intervals.py)  
    - [Merge Sorted Array](/algorithms/arrays/merge_sorted_array.py)  
    - [Move Zeroes](/algorithms/arrays/move_zeroes.py)  
    - [Number Plus One](/algorithms/arrays/number_plus_one.py)  
    - [Place Flowers](/algorithms/arrays/place_flowers.py)  
    - [Remove Duplicates Two](/algorithms/arrays/remove_duplicates_two.py)  
    - [Rotate Array](/algorithms/arrays/rotate_array.py)  
    - [Summary Ranges](/algorithms/arrays/summary_ranges.py)  
    - [Third Max Number](/algorithms/arrays/third_max_number.py)  
    - [Two Sum Sorted Array](/algorithms/arrays/two_sum_sorted_array.py)  
  
* [**Backtracking**](/algorithms/backtracking)  
    - [Combinations Sum Two](/algorithms/backtracking/combinations_sum_two.py)  
    - [Combinations Sum](/algorithms/backtracking/combinations_sum.py)  
    - [Combinations](/algorithms/backtracking/combinations.py)  
    - [Generate Paranthesis](/algorithms/backtracking/generate_paranthesis.py)  
    - [Letter Combinations](/algorithms/backtracking/letter_combinations.py)  
    - [Permutations One](/algorithms/backtracking/permutations_one.py)  
    - [Permutations Two](/algorithms/backtracking/permutations_two.py)  
    - [Subsets Duplicates](/algorithms/backtracking/subsets_duplicates.py)  
    - [Subsets](/algorithms/backtracking/subsets.py)  
  
* [**Binarysearch**](/algorithms/binarysearch)  
    - [Binary Search](/algorithms/binarysearch/binary_search.py)  
    - [Find K Closest](/algorithms/binarysearch/find_k_closest.py)  
    - [Find Peak](/algorithms/binarysearch/find_peak.py)  
    - [First Bad](/algorithms/binarysearch/first_bad.py)  
    - [Guess Number](/algorithms/binarysearch/guess_number.py)  
    - [Min In Rotated Sorted Array](/algorithms/binarysearch/min_in_rotated_sorted_array.py)  
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
    - [List To Bst](/algorithms/bst/list_to_bst.py)  
    - [Recover Bst](/algorithms/bst/recover_bst.py)  
    - [Validate Bst](/algorithms/bst/validate_bst.py)  
  
* [**Dynamic Programming**](/algorithms/dp)  
    - [Climbing Stairs](/algorithms/dp/climbing_stairs.py)  
    - [Delete Operations For Two Strings](/algorithms/dp/delete_operations_for_two_strings.py)  
    - [Fibonacci](/algorithms/dp/fibonacci.py)  
    - [Kth Grammar](/algorithms/dp/kth_grammar.py)  
    - [Longest Common Subsequence](/algorithms/dp/longest_common_subsequence.py)  
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
    - [Word Search](/algorithms/graphs/word_search.py)  
  
* [**Hash Tables**](/algorithms/hashtables)  
    - [*Hashmap Implementation*](/algorithms/hashtables/hashmap_implementation.py)  
    - [Bulls And Cows](/algorithms/hashtables/bulls_and_cows.py)  
    - [Four Sum](/algorithms/hashtables/four_sum.py)  
    - [Group Anagrams](/algorithms/hashtables/group_anagrams.py)  
    - [Repeated Dna Sequences](/algorithms/hashtables/repeated_dna_sequences.py)  
    - [Shuffle Array](/algorithms/hashtables/shuffle_array.py)  
    - [Substring Concat](/algorithms/hashtables/substring_concat.py)  
    - [Three Sum](/algorithms/hashtables/three_sum.py)  
    - [Two Sum](/algorithms/hashtables/two_sum.py)  
    - [Valid Sudoku](/algorithms/hashtables/valid_sudoku.py)  
    - [Word Pattern](/algorithms/hashtables/word_pattern.py)  
  
* [**Heaps**](/algorithms/heaps)  
    - [*Heap Implementation*](/algorithms/heaps/heap_implementation.py)  
    - [K Most Frequent](/algorithms/heaps/k_most_frequent.py)  
    - [Kth Largest](/algorithms/heaps/kth_largest.py)  
  
* [**Linked List**](/algorithms/linkedlist)  
    - [*Singly Linked List Implementation*](/algorithms/linkedlist/singly_linked_list_implementation.py)  
    - [Add Two Numbers](/algorithms/linkedlist/add_two_numbers.py)  
    - [Delete Duplicates All](/algorithms/linkedlist/delete_duplicates_all.py)  
    - [Delete Duplicates](/algorithms/linkedlist/delete_duplicates.py)  
    - [Delete Node Without Head](/algorithms/linkedlist/delete_node_without_head.py)  
    - [Intersection](/algorithms/linkedlist/intersection.py)  
    - [Linked Cycle](/algorithms/linkedlist/linked_cycle.py)  
    - [List Palindrome](/algorithms/linkedlist/list_palindrome.py)  
    - [Merge K Lists](/algorithms/linkedlist/merge_k_lists.py)  
    - [Merge Two Lists](/algorithms/linkedlist/merge_two_lists.py)  
    - [Odd Even Linked List](/algorithms/linkedlist/odd_even_linked_list.py)  
    - [Remove Element](/algorithms/linkedlist/remove_element.py)  
    - [Remove Nth End](/algorithms/linkedlist/remove_nth_end.py)  
    - [Reorder List](/algorithms/linkedlist/reorder_list.py)  
    - [Reverse K Groups](/algorithms/linkedlist/reverse_k_groups.py)  
    - [Reverse Linkedlist](/algorithms/linkedlist/reverse_linkedlist.py)  
    - [Reverse Mn](/algorithms/linkedlist/reverse_mn.py)  
    - [Rotate List](/algorithms/linkedlist/rotate_list.py)  
    - [Swap Pairs](/algorithms/linkedlist/swap_pairs.py)  
  
* [**Math**](/algorithms/math)  
    - [Add Binary](/algorithms/math/add_binary.py)  
    - [Add Digits](/algorithms/math/add_digits.py)  
    - [Convert To Number](/algorithms/math/convert_to_number.py)  
    - [Count Primes](/algorithms/math/count_primes.py)  
    - [Count Zeroes Factorial](/algorithms/math/count_zeroes_factorial.py)  
    - [Divide Two Numbers](/algorithms/math/divide_two_numbers.py)  
    - [Game Of Nim](/algorithms/math/game_of_nim.py)  
    - [Happy Numbers](/algorithms/math/happy_numbers.py)  
    - [Intersection Two Arrays](/algorithms/math/intersection_two_arrays.py)  
    - [Majority Element](/algorithms/math/majority_element.py)  
    - [Missing Number](/algorithms/math/missing_number.py)  
    - [Next Permutation](/algorithms/math/next_permutation.py)  
    - [Num To Col](/algorithms/math/num_to_col.py)  
    - [Power Of Two](/algorithms/math/power_of_two.py)  
    - [Ugly Numbers](/algorithms/math/ugly_numbers.py)  
    - [Valid Number](/algorithms/math/valid_number.py)  
  
* [**Matrix**](/algorithms/matrix)  
    - [Reshape Matrix](/algorithms/matrix/reshape_matrix.py)  
    - [Rotate Image](/algorithms/matrix/rotate_image.py)  
    - [Spiral Matrix Generate](/algorithms/matrix/spiral_matrix_generate.py)  
    - [Spiral Matrix](/algorithms/matrix/spiral_matrix.py)  
  
* [**Queues**](/algorithms/queues)  
    - [*Queue Implementation*](/algorithms/queues/queue_implementation.py)  
    - [Gas Station](/algorithms/queues/gas_station.py)  
    - [Queue Using Stacks](/algorithms/queues/queue_using_stacks.py)  
    - [Stack Using Queues](/algorithms/queues/stack_using_queues.py)  
  
* [**Stack**](/algorithms/stack)  
    - [Evaluate Reverse Polish Notation](/algorithms/stack/evaluate_reverse_polish_notation.py)  
    - [Min Stack](/algorithms/stack/min_stack.py)  
    - [Simplify Path](/algorithms/stack/simplify_path.py)  
    - [Valid Paran](/algorithms/stack/valid_paran.py)  
  
* [**Strings**](/algorithms/strings)  
    - [Add Binary](/algorithms/strings/add_binary.py)  
    - [Add Strings](/algorithms/strings/add_strings.py)  
    - [Compare Version Numbers](/algorithms/strings/compare_version_numbers.py)  
    - [Count Say](/algorithms/strings/count_say.py)  
    - [Decode String](/algorithms/strings/decode_string.py)  
    - [First Unique Character](/algorithms/strings/first_unique_character.py)  
    - [Goat Latin](/algorithms/strings/goat_latin.py)  
    - [Int To Roman](/algorithms/strings/int_to_roman.py)  
    - [Isomorphic](/algorithms/strings/isomorphic.py)  
    - [Jewels](/algorithms/strings/jewels.py)  
    - [Largest Number](/algorithms/strings/largest_number.py)  
    - [Length Of Last Word](/algorithms/strings/length_of_last_word.py)  
    - [Longest Common Prefix](/algorithms/strings/longest_common_prefix.py)  
    - [Longest Palin Substring](/algorithms/strings/longest_palin_substring.py)  
    - [Longest Substring Without Repeating](/algorithms/strings/longest_substring_without_repeating.py)  
    - [Multiply Strings](/algorithms/strings/multiply_strings.py)  
    - [Number Of Segments String](/algorithms/strings/number_of_segments_string.py)  
    - [Palindrome](/algorithms/strings/palindrome.py)  
    - [Permutations In String](/algorithms/strings/permutations_in_string.py)  
    - [Ransom Note](/algorithms/strings/ransom_note.py)  
    - [Reverse Int](/algorithms/strings/reverse_int.py)  
    - [Reverse Only Letters](/algorithms/strings/reverse_only_letters.py)  
    - [Reverse String Ii](/algorithms/strings/reverse_string_II.py)  
    - [Reverse String Words](/algorithms/strings/reverse_string_words.py)  
    - [Reverse String](/algorithms/strings/reverse_string.py)  
    - [Reverse Vowels Strings](/algorithms/strings/reverse_vowels_strings.py)  
    - [Reverse Words Iii](/algorithms/strings/reverse_words_III.py)  
    - [Robot Origin](/algorithms/strings/robot_origin.py)  
    - [Roman To Int](/algorithms/strings/roman_to_int.py)  
    - [String Compression](/algorithms/strings/string_compression.py)  
    - [String To Integer](/algorithms/strings/string_to_integer.py)  
    - [Strstr](/algorithms/strings/strstr.py)  
    - [To Lower](/algorithms/strings/to_lower.py)  
    - [Unique Email](/algorithms/strings/unique_email.py)  
    - [Unique Morse Code](/algorithms/strings/unique_morse_code.py)  
    - [Valid Anagram](/algorithms/strings/valid_anagram.py)  
    - [Valid Ip](/algorithms/strings/valid_ip.py)  
    - [Valid Palin](/algorithms/strings/valid_palin.py)  
    - [Zigzag Conversion](/algorithms/strings/zigzag_conversion.py)  
  
* [**Trees**](/algorithms/trees)  
    - [*Tree Implementation*](/algorithms/trees/tree_implementation.py)  
    - [*Trie Implementation*](/algorithms/trees/trie_implementation.py)  
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
    - [Populate Next Right Pointer](/algorithms/trees/populate_next_right_pointer.py)  
    - [Postorder](/algorithms/trees/postorder.py)  
    - [Preorder](/algorithms/trees/preorder.py)  
    - [Same Tree](/algorithms/trees/same_tree.py)  
    - [Sum Root To Leaf Paths](/algorithms/trees/sum_root_to_leaf_paths.py)  
    - [Symmetric](/algorithms/trees/symmetric.py)  
    - [Tree Paths](/algorithms/trees/tree_paths.py)  
    - [Zigzag Level Order](/algorithms/trees/zigzag_level_order.py)  
  
* [**Trie**](/algorithms/trie)  
    - [*Trie Implementation*](/algorithms/trie/trie_implementation.py)  
  
* [**Two Pointers**](/algorithms/twopointers)  
    - [Container With Most Water](/algorithms/twopointers/container_with_most_water.py)  
    - [Remove Duplicates](/algorithms/twopointers/remove_duplicates.py)  
    - [Remove Element](/algorithms/twopointers/remove_element.py)  
    - [Three Sum Closest](/algorithms/twopointers/three_sum_closest.py)  
  
