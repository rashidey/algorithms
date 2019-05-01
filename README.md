
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
**Data Structures** : 12  
**Algorithms** &nbsp; &nbsp; &nbsp; &nbsp; : 336

## List of Implementations



* [**Arrays**](/algorithms/arrays)  
    - [*Dynamic Array Implementation*](/algorithms/arrays/dynamic_array_implementation.py)  
    - [Array Partition](/algorithms/arrays/array_partition.py)  
    - [Assign Cookies](/algorithms/arrays/assign_cookies.py)  
    - [Best Time To Buy Stock Ii](/algorithms/arrays/best_time_to_buy_stock_II.py)  
    - [Best Time To Buy Stock](/algorithms/arrays/best_time_to_buy_stock.py)  
    - [Contains Duplicate One](/algorithms/arrays/contains_duplicate_one.py)  
    - [Contains Duplicate Range](/algorithms/arrays/contains_duplicate_range.py)  
    - [Degree Array](/algorithms/arrays/degree_array.py)  
    - [Distribute Candies](/algorithms/arrays/distribute_candies.py)  
    - [Find All Dissapeared Numbers](/algorithms/arrays/find_all_dissapeared_numbers.py)  
    - [Find All Duplicates](/algorithms/arrays/find_all_duplicates.py)  
    - [Find Pivot Index](/algorithms/arrays/find_pivot_index.py)  
    - [First Missing Positive](/algorithms/arrays/first_missing_positive.py)  
    - [Friends Of Ages](/algorithms/arrays/friends_of_ages.py)  
    - [Intersection Two Arrays Ii](/algorithms/arrays/intersection_two_arrays_II.py)  
    - [K Diff Pairs](/algorithms/arrays/k_diff_pairs.py)  
    - [Largest Number Twice Of Others](/algorithms/arrays/largest_number_twice_of_others.py)  
    - [Longest Continuous Increasing Subsequence](/algorithms/arrays/longest_continuous_increasing_subsequence.py)  
    - [Max Average Subarray](/algorithms/arrays/max_average_subarray.py)  
    - [Max Consecutive Ones](/algorithms/arrays/max_consecutive_ones.py)  
    - [Max Product Three Numbers](/algorithms/arrays/max_product_three_numbers.py)  
    - [Maximize Distance To Nearest Person](/algorithms/arrays/maximize_distance_to_nearest_person.py)  
    - [Maximum Subarray](/algorithms/arrays/maximum_subarray.py)  
    - [Merge Intervals](/algorithms/arrays/merge_intervals.py)  
    - [Merge Sorted Array](/algorithms/arrays/merge_sorted_array.py)  
    - [Minimum Moves To Equal Array](/algorithms/arrays/minimum_moves_to_equal_array.py)  
    - [Move Zeroes](/algorithms/arrays/move_zeroes.py)  
    - [Next Greater Element](/algorithms/arrays/next_greater_element.py)  
    - [Non Decreasing Array](/algorithms/arrays/non_decreasing_array.py)  
    - [Number Plus One](/algorithms/arrays/number_plus_one.py)  
    - [Partition Array In Three](/algorithms/arrays/partition_array_in_three.py)  
    - [Place Flowers](/algorithms/arrays/place_flowers.py)  
    - [Positions Large Groups](/algorithms/arrays/positions_large_groups.py)  
    - [Remove Duplicates Two](/algorithms/arrays/remove_duplicates_two.py)  
    - [Rotate Array](/algorithms/arrays/rotate_array.py)  
    - [Set Mismatch](/algorithms/arrays/set_mismatch.py)  
    - [Shortest Unsorted Subarray](/algorithms/arrays/shortest_unsorted_subarray.py)  
    - [Summary Ranges](/algorithms/arrays/summary_ranges.py)  
    - [Third Max Number](/algorithms/arrays/third_max_number.py)  
    - [Two Sum Sorted Array](/algorithms/arrays/two_sum_sorted_array.py)  
  
* [**Backtracking**](/algorithms/backtracking)  
    - [Binary Watch](/algorithms/backtracking/binary_watch.py)  
    - [Combinations Sum Three](/algorithms/backtracking/combinations_sum_three.py)  
    - [Combinations Sum Two](/algorithms/backtracking/combinations_sum_two.py)  
    - [Combinations Sum](/algorithms/backtracking/combinations_sum.py)  
    - [Combinations](/algorithms/backtracking/combinations.py)  
    - [Generate Paranthesis](/algorithms/backtracking/generate_paranthesis.py)  
    - [Letter Combinations](/algorithms/backtracking/letter_combinations.py)  
    - [Matchsticks To Square](/algorithms/backtracking/matchsticks_to_square.py)  
    - [Permutations One](/algorithms/backtracking/permutations_one.py)  
    - [Permutations Two](/algorithms/backtracking/permutations_two.py)  
    - [Subsets Duplicates](/algorithms/backtracking/subsets_duplicates.py)  
    - [Subsets](/algorithms/backtracking/subsets.py)  
  
* [**Binarysearch**](/algorithms/binarysearch)  
    - [Arranging Coins](/algorithms/binarysearch/arranging_coins.py)  
    - [Binary Search](/algorithms/binarysearch/binary_search.py)  
    - [Find K Closest](/algorithms/binarysearch/find_k_closest.py)  
    - [Find Peak](/algorithms/binarysearch/find_peak.py)  
    - [First Bad](/algorithms/binarysearch/first_bad.py)  
    - [Guess Number](/algorithms/binarysearch/guess_number.py)  
    - [Min In Rotated Sorted Array](/algorithms/binarysearch/min_in_rotated_sorted_array.py)  
    - [Peak Index Mountain Array](/algorithms/binarysearch/peak_index_mountain_array.py)  
    - [Search 2D Matrix](/algorithms/binarysearch/search_2d_matrix.py)  
    - [Search Insert Position](/algorithms/binarysearch/search_insert_position.py)  
    - [Search Range](/algorithms/binarysearch/search_range.py)  
    - [Search Rotated Array Ii](/algorithms/binarysearch/search_rotated_array_II.py)  
    - [Search Rotated Array](/algorithms/binarysearch/search_rotated_array.py)  
    - [Sqrt Number](/algorithms/binarysearch/sqrt_number.py)  
    - [Valid Perfect Square](/algorithms/binarysearch/valid_perfect_square.py)  
  
* [**Bits**](/algorithms/bits)  
    - [Single Number](/algorithms/bits/single_number.py)  
  
* [**Binary Search Tree**](/algorithms/bst)  
    - [*Bst Implementation*](/algorithms/bst/bst_implementation.py)  
    - [Bst Iterator](/algorithms/bst/bst_iterator.py)  
    - [Delete Node](/algorithms/bst/delete_node.py)  
    - [Find Mode Bst](/algorithms/bst/find_mode_bst.py)  
    - [Increasing Order Search Tree](/algorithms/bst/increasing_order_search_tree.py)  
    - [Kth Smallest Element](/algorithms/bst/kth_smallest_element.py)  
    - [List To Bst](/algorithms/bst/list_to_bst.py)  
    - [Lowest Common Ancestor Bst](/algorithms/bst/lowest_common_ancestor_bst.py)  
    - [Minimum Diff Bst](/algorithms/bst/minimum_diff_bst.py)  
    - [Recover Bst](/algorithms/bst/recover_bst.py)  
    - [Search Bst](/algorithms/bst/search_bst.py)  
    - [Validate Bst](/algorithms/bst/validate_bst.py)  
  
* [**Dynamic Programming**](/algorithms/dp)  
    - [Climbing Stairs](/algorithms/dp/climbing_stairs.py)  
    - [Continuous Subarray Sum](/algorithms/dp/continuous_subarray_sum.py)  
    - [Delete Operations For Two Strings](/algorithms/dp/delete_operations_for_two_strings.py)  
    - [Fibonacci](/algorithms/dp/fibonacci.py)  
    - [House Robber](/algorithms/dp/house_robber.py)  
    - [Integer Replacement](/algorithms/dp/integer_replacement.py)  
    - [Kth Grammar](/algorithms/dp/kth_grammar.py)  
    - [Longest Common Subsequence](/algorithms/dp/longest_common_subsequence.py)  
    - [Longest Increasing Subsequence](/algorithms/dp/longest_increasing_subsequence.py)  
    - [Min Cost Climbing Stairs](/algorithms/dp/min_cost_climbing_stairs.py)  
    - [Minimum Path Sum](/algorithms/dp/minimum_path_sum.py)  
    - [Nth Ugly Number](/algorithms/dp/nth_ugly_number.py)  
    - [Pascal Row](/algorithms/dp/pascal_row.py)  
    - [Pascal](/algorithms/dp/pascal.py)  
    - [Pow](/algorithms/dp/pow.py)  
    - [Range Sum Query](/algorithms/dp/range_sum_query.py)  
    - [Super Ugly Number](/algorithms/dp/super_ugly_number.py)  
    - [Triangle Min Path](/algorithms/dp/triangle_min_path.py)  
    - [Unique Paths With Obstacle](/algorithms/dp/unique_paths_with_obstacle.py)  
    - [Unique Paths](/algorithms/dp/unique_paths.py)  
    - [Zero One Matrix](/algorithms/dp/zero_one_matrix.py)  
  
* [**Graphs**](/algorithms/graphs)  
    - [*Graph Implementation*](/algorithms/graphs/graph_implementation.py)  
    - [Bt Right View](/algorithms/graphs/bt_right_view.py)  
    - [Clone Graph](/algorithms/graphs/clone_graph.py)  
    - [Concatenated Words](/algorithms/graphs/concatenated_words.py)  
    - [Course Order](/algorithms/graphs/course_order.py)  
    - [Employee Importance](/algorithms/graphs/employee_importance.py)  
    - [Flood Fill](/algorithms/graphs/flood_fill.py)  
    - [Friend Circle](/algorithms/graphs/friend_circle.py)  
    - [House Robber Three](/algorithms/graphs/house_robber_three.py)  
    - [Is Bipartate](/algorithms/graphs/is_bipartate.py)  
    - [Jump Game Ii](/algorithms/graphs/jump_game_II.py)  
    - [Make Larger Island](/algorithms/graphs/make_larger_island.py)  
    - [Max Area Island](/algorithms/graphs/max_area_island.py)  
    - [Minesweeper](/algorithms/graphs/minesweeper.py)  
    - [Number Islands](/algorithms/graphs/number_islands.py)  
    - [Pacific Atlantic Water Flow](/algorithms/graphs/pacific_atlantic_water_flow.py)  
    - [Rotton Oranges](/algorithms/graphs/rotton_oranges.py)  
    - [Surround Region](/algorithms/graphs/surround_region.py)  
    - [Word Ladder Two](/algorithms/graphs/word_ladder_two.py)  
    - [Word Ladder](/algorithms/graphs/word_ladder.py)  
    - [Word Search](/algorithms/graphs/word_search.py)  
  
* [**Greedy**](/algorithms/greedy)  
    - [Burst Balloons](/algorithms/greedy/burst_balloons.py)  
    - [Dota2 Senate](/algorithms/greedy/dota2_senate.py)  
    - [Is Subsequence](/algorithms/greedy/is_subsequence.py)  
    - [Make Paran Valid](/algorithms/greedy/make_paran_valid.py)  
    - [Moving Stones](/algorithms/greedy/moving_stones.py)  
    - [Non Overlapping Intervals](/algorithms/greedy/non_overlapping_intervals.py)  
    - [Queue Reconstruction By Height](/algorithms/greedy/queue_reconstruction_by_height.py)  
    - [Reorganize String](/algorithms/greedy/reorganize_string.py)  
  
* [**Hash Tables**](/algorithms/hashtables)  
    - [*Hashmap Implementation*](/algorithms/hashtables/hashmap_implementation.py)  
    - [Banned Words](/algorithms/hashtables/banned_words.py)  
    - [Bulls And Cows](/algorithms/hashtables/bulls_and_cows.py)  
    - [Encode Decode](/algorithms/hashtables/encode_decode.py)  
    - [Find Common Characters](/algorithms/hashtables/find_common_characters.py)  
    - [Four Sum](/algorithms/hashtables/four_sum.py)  
    - [Fraction To Decimal](/algorithms/hashtables/fraction_to_decimal.py)  
    - [Group Anagrams](/algorithms/hashtables/group_anagrams.py)  
    - [Hashmap](/algorithms/hashtables/hashmap.py)  
    - [Hashset](/algorithms/hashtables/hashset.py)  
    - [Keyboard Row](/algorithms/hashtables/keyboard_row.py)  
    - [Lru Cache](/algorithms/hashtables/lru_cache.py)  
    - [Magic Dictionary](/algorithms/hashtables/magic_dictionary.py)  
    - [Minimum Index Sum Of Two Lists](/algorithms/hashtables/minimum_index_sum_of_two_lists.py)  
    - [Repeated Dna Sequences](/algorithms/hashtables/repeated_dna_sequences.py)  
    - [Shortest Completing Word](/algorithms/hashtables/shortest_completing_word.py)  
    - [Shuffle Array](/algorithms/hashtables/shuffle_array.py)  
    - [Sort By Count](/algorithms/hashtables/sort_by_count.py)  
    - [Subdomain Visit Count](/algorithms/hashtables/subdomain_visit_count.py)  
    - [Substring Concat](/algorithms/hashtables/substring_concat.py)  
    - [Three Sum](/algorithms/hashtables/three_sum.py)  
    - [Two Sum](/algorithms/hashtables/two_sum.py)  
    - [Uncommon Words](/algorithms/hashtables/uncommon_words.py)  
    - [Valid Sudoku](/algorithms/hashtables/valid_sudoku.py)  
    - [Verifying Alien Dictionary](/algorithms/hashtables/verifying_alien_dictionary.py)  
    - [Word Pattern](/algorithms/hashtables/word_pattern.py)  
  
* [**Heaps**](/algorithms/heaps)  
    - [*Heap Implementation*](/algorithms/heaps/heap_implementation.py)  
    - [Design Twitter](/algorithms/heaps/design_twitter.py)  
    - [K Most Frequent](/algorithms/heaps/k_most_frequent.py)  
    - [K Pairs With Smallest Sums](/algorithms/heaps/k_pairs_with_smallest_sums.py)  
    - [Kth Largest In Stream](/algorithms/heaps/kth_largest_in_stream.py)  
    - [Kth Largest](/algorithms/heaps/kth_largest.py)  
    - [Kth Smallest In Sorted Matrix](/algorithms/heaps/kth_smallest_in_sorted_matrix.py)  
    - [Top K Frequent Words](/algorithms/heaps/top_k_frequent_words.py)  
  
* [**Linked List**](/algorithms/linkedlist)  
    - [*Singly Linked List Implementation*](/algorithms/linkedlist/singly_linked_list_implementation.py)  
    - [Add Two Numbers Ii](/algorithms/linkedlist/add_two_numbers_II.py)  
    - [Add Two Numbers](/algorithms/linkedlist/add_two_numbers.py)  
    - [Delete Duplicates All](/algorithms/linkedlist/delete_duplicates_all.py)  
    - [Delete Duplicates](/algorithms/linkedlist/delete_duplicates.py)  
    - [Delete Node Without Head](/algorithms/linkedlist/delete_node_without_head.py)  
    - [Intersection](/algorithms/linkedlist/intersection.py)  
    - [Linked Cycle](/algorithms/linkedlist/linked_cycle.py)  
    - [Linked List Cycle Ii](/algorithms/linkedlist/linked_list_cycle_II.py)  
    - [Linkedlist](/algorithms/linkedlist/linkedlist.py)  
    - [List Palindrome](/algorithms/linkedlist/list_palindrome.py)  
    - [Merge K Lists](/algorithms/linkedlist/merge_k_lists.py)  
    - [Merge Two Lists](/algorithms/linkedlist/merge_two_lists.py)  
    - [Middle Linked List](/algorithms/linkedlist/middle_linked_list.py)  
    - [Odd Even Linked List](/algorithms/linkedlist/odd_even_linked_list.py)  
    - [Partition List](/algorithms/linkedlist/partition_list.py)  
    - [Remove Element](/algorithms/linkedlist/remove_element.py)  
    - [Remove Nth End](/algorithms/linkedlist/remove_nth_end.py)  
    - [Reorder List](/algorithms/linkedlist/reorder_list.py)  
    - [Reverse K Groups](/algorithms/linkedlist/reverse_k_groups.py)  
    - [Reverse Linkedlist](/algorithms/linkedlist/reverse_linkedlist.py)  
    - [Reverse Mn](/algorithms/linkedlist/reverse_mn.py)  
    - [Rotate List](/algorithms/linkedlist/rotate_list.py)  
    - [Sort List](/algorithms/linkedlist/sort_list.py)  
    - [Swap Pairs](/algorithms/linkedlist/swap_pairs.py)  
  
* [**Math**](/algorithms/math)  
    - [Add Binary](/algorithms/math/add_binary.py)  
    - [Add Digits](/algorithms/math/add_digits.py)  
    - [Basic Calculator I](/algorithms/math/basic_calculator_I.py)  
    - [Basic Calculator Ii](/algorithms/math/basic_calculator_II.py)  
    - [Construct Rectangle](/algorithms/math/construct_rectangle.py)  
    - [Convert To Number](/algorithms/math/convert_to_number.py)  
    - [Count Primes](/algorithms/math/count_primes.py)  
    - [Count Zeroes Factorial](/algorithms/math/count_zeroes_factorial.py)  
    - [Divide Two Numbers](/algorithms/math/divide_two_numbers.py)  
    - [Game Of Nim](/algorithms/math/game_of_nim.py)  
    - [Hamming Distance](/algorithms/math/hamming_distance.py)  
    - [Happy Numbers](/algorithms/math/happy_numbers.py)  
    - [Intersection Two Arrays](/algorithms/math/intersection_two_arrays.py)  
    - [Majority Element](/algorithms/math/majority_element.py)  
    - [Min Time Difference](/algorithms/math/min_time_difference.py)  
    - [Missing Number](/algorithms/math/missing_number.py)  
    - [Next Permutation](/algorithms/math/next_permutation.py)  
    - [Nth Digit](/algorithms/math/nth_digit.py)  
    - [Num To Col](/algorithms/math/num_to_col.py)  
    - [Perfect Number](/algorithms/math/perfect_number.py)  
    - [Power Of Two](/algorithms/math/power_of_two.py)  
    - [Self Dividing Numbers](/algorithms/math/self_dividing_numbers.py)  
    - [Total Time](/algorithms/math/total_time.py)  
    - [Ugly Numbers](/algorithms/math/ugly_numbers.py)  
    - [Valid Number](/algorithms/math/valid_number.py)  
  
* [**Matrix**](/algorithms/matrix)  
    - [Flip Image](/algorithms/matrix/flip_image.py)  
    - [Game Of Life](/algorithms/matrix/game_of_life.py)  
    - [Image Smoother](/algorithms/matrix/image_smoother.py)  
    - [Island Perimeter](/algorithms/matrix/island_perimeter.py)  
    - [Magic Squares In Grid](/algorithms/matrix/magic_squares_in_grid.py)  
    - [Range Addition](/algorithms/matrix/range_addition.py)  
    - [Reshape Matrix](/algorithms/matrix/reshape_matrix.py)  
    - [Rotate Image](/algorithms/matrix/rotate_image.py)  
    - [Set Matrix Zeros](/algorithms/matrix/set_matrix_zeros.py)  
    - [Spiral Matrix Generate](/algorithms/matrix/spiral_matrix_generate.py)  
    - [Spiral Matrix](/algorithms/matrix/spiral_matrix.py)  
    - [Toeplitz Matrix](/algorithms/matrix/toeplitz_matrix.py)  
    - [Transpose Matrix](/algorithms/matrix/transpose_matrix.py)  
  
* [**Queues**](/algorithms/queues)  
    - [*Circular Deque Implementation*](/algorithms/queues/circular_deque_implementation.py)  
    - [*Circular Queue Implementation*](/algorithms/queues/circular_queue_implementation.py)  
    - [*Queue Implementation*](/algorithms/queues/queue_implementation.py)  
    - [Gas Station](/algorithms/queues/gas_station.py)  
    - [Max Sliding Window](/algorithms/queues/max_sliding_window.py)  
    - [Queue Using Stacks](/algorithms/queues/queue_using_stacks.py)  
    - [Stack Using Queues](/algorithms/queues/stack_using_queues.py)  
  
* [**Sort**](/algorithms/sort)  
    - [Bubble Sort](/algorithms/sort/bubble_sort.py)  
    - [Insertion Sort](/algorithms/sort/insertion_sort.py)  
    - [Merge Sort](/algorithms/sort/merge_sort.py)  
    - [Most Profit Workers](/algorithms/sort/most_profit_workers.py)  
    - [Quick Sort](/algorithms/sort/quick_sort.py)  
    - [Selection Sort](/algorithms/sort/selection_sort.py)  
    - [Sort Three Colors](/algorithms/sort/sort_three_colors.py)  
  
* [**Stack**](/algorithms/stack)  
    - [Baseball Game](/algorithms/stack/baseball_game.py)  
    - [Evaluate Reverse Polish Notation](/algorithms/stack/evaluate_reverse_polish_notation.py)  
    - [Exclusive Fuction Time](/algorithms/stack/exclusive_fuction_time.py)  
    - [Min Stack](/algorithms/stack/min_stack.py)  
    - [Next Greater Element Ii](/algorithms/stack/next_greater_element_II.py)  
    - [One Three Two Pattern](/algorithms/stack/one_three_two_pattern.py)  
    - [Simplify Path](/algorithms/stack/simplify_path.py)  
    - [Valid Paran](/algorithms/stack/valid_paran.py)  
  
* [**Strings**](/algorithms/strings)  
    - [Add Binary](/algorithms/strings/add_binary.py)  
    - [Add Strings](/algorithms/strings/add_strings.py)  
    - [Backspace Compare](/algorithms/strings/backspace_compare.py)  
    - [Buddy Strings](/algorithms/strings/buddy_strings.py)  
    - [Compare Version Numbers](/algorithms/strings/compare_version_numbers.py)  
    - [Complex Number Multiplication](/algorithms/strings/complex_number_multiplication.py)  
    - [Count Say](/algorithms/strings/count_say.py)  
    - [Decode String](/algorithms/strings/decode_string.py)  
    - [Detect Capital](/algorithms/strings/detect_capital.py)  
    - [Find All Anagrams](/algorithms/strings/find_all_anagrams.py)  
    - [Find Duplicate Files](/algorithms/strings/find_duplicate_files.py)  
    - [First Unique Character](/algorithms/strings/first_unique_character.py)  
    - [Goat Latin](/algorithms/strings/goat_latin.py)  
    - [Int To Roman](/algorithms/strings/int_to_roman.py)  
    - [Isomorphic](/algorithms/strings/isomorphic.py)  
    - [Jewels](/algorithms/strings/jewels.py)  
    - [Largest Number](/algorithms/strings/largest_number.py)  
    - [Length Of Last Word](/algorithms/strings/length_of_last_word.py)  
    - [Longest Common Prefix](/algorithms/strings/longest_common_prefix.py)  
    - [Longest Palin Substring](/algorithms/strings/longest_palin_substring.py)  
    - [Longest Palindrome](/algorithms/strings/longest_palindrome.py)  
    - [Longest Substring Without Repeating](/algorithms/strings/longest_substring_without_repeating.py)  
    - [Longest Uncommon Seq](/algorithms/strings/longest_uncommon_seq.py)  
    - [Multiply Strings](/algorithms/strings/multiply_strings.py)  
    - [Number Of Segments String](/algorithms/strings/number_of_segments_string.py)  
    - [Optimal Division](/algorithms/strings/optimal_division.py)  
    - [Palindrome](/algorithms/strings/palindrome.py)  
    - [Permutations In String](/algorithms/strings/permutations_in_string.py)  
    - [Ransom Note](/algorithms/strings/ransom_note.py)  
    - [Remove Comments](/algorithms/strings/remove_comments.py)  
    - [Repeated String Match](/algorithms/strings/repeated_string_match.py)  
    - [Repeated Substring Pattern](/algorithms/strings/repeated_substring_pattern.py)  
    - [Reverse Int](/algorithms/strings/reverse_int.py)  
    - [Reverse Only Letters](/algorithms/strings/reverse_only_letters.py)  
    - [Reverse String Ii](/algorithms/strings/reverse_string_II.py)  
    - [Reverse String Words](/algorithms/strings/reverse_string_words.py)  
    - [Reverse String](/algorithms/strings/reverse_string.py)  
    - [Reverse Vowels Strings](/algorithms/strings/reverse_vowels_strings.py)  
    - [Reverse Words Iii](/algorithms/strings/reverse_words_III.py)  
    - [Robot Origin](/algorithms/strings/robot_origin.py)  
    - [Roman To Int](/algorithms/strings/roman_to_int.py)  
    - [Rotated Digits](/algorithms/strings/rotated_digits.py)  
    - [String Compression](/algorithms/strings/string_compression.py)  
    - [String To Integer](/algorithms/strings/string_to_integer.py)  
    - [Strstr](/algorithms/strings/strstr.py)  
    - [To Lower](/algorithms/strings/to_lower.py)  
    - [Unique Email](/algorithms/strings/unique_email.py)  
    - [Unique Morse Code](/algorithms/strings/unique_morse_code.py)  
    - [Valid Anagram](/algorithms/strings/valid_anagram.py)  
    - [Valid Ip](/algorithms/strings/valid_ip.py)  
    - [Valid Palin](/algorithms/strings/valid_palin.py)  
    - [Valid Palindrome Ii](/algorithms/strings/valid_palindrome_II.py)  
    - [Zigzag Conversion](/algorithms/strings/zigzag_conversion.py)  
  
* [**Trees**](/algorithms/trees)  
    - [*Tree Implementation*](/algorithms/trees/tree_implementation.py)  
    - [*Trie Implementation*](/algorithms/trees/trie_implementation.py)  
    - [Array Bst](/algorithms/trees/array_bst.py)  
    - [Average Levels](/algorithms/trees/average_levels.py)  
    - [Bst To Greater Tree](/algorithms/trees/bst_to_greater_tree.py)  
    - [Build Tree Postorder](/algorithms/trees/build_tree_postorder.py)  
    - [Construct Pre In](/algorithms/trees/construct_pre_in.py)  
    - [Cousins In Binary Trees](/algorithms/trees/cousins_in_binary_trees.py)  
    - [Find Bottom Left](/algorithms/trees/find_bottom_left.py)  
    - [Flatten Binary Tree To Linked List](/algorithms/trees/flatten_binary_tree_to_linked_list.py)  
    - [Inorder](/algorithms/trees/inorder.py)  
    - [Invert Tree](/algorithms/trees/invert_tree.py)  
    - [Is Balanced](/algorithms/trees/is_balanced.py)  
    - [Largest Value Level](/algorithms/trees/largest_value_level.py)  
    - [Left Similar Trees](/algorithms/trees/left_similar_trees.py)  
    - [Level Order One](/algorithms/trees/level_order_one.py)  
    - [Level Order Two](/algorithms/trees/level_order_two.py)  
    - [Lowest Common Ancestor](/algorithms/trees/lowest_common_ancestor.py)  
    - [Max Depth](/algorithms/trees/max_depth.py)  
    - [Maximum Path Sum](/algorithms/trees/maximum_path_sum.py)  
    - [Merge Two Trees](/algorithms/trees/merge_two_trees.py)  
    - [Min Depth](/algorithms/trees/min_depth.py)  
    - [Path Sum All](/algorithms/trees/path_sum_all.py)  
    - [Path Sum](/algorithms/trees/path_sum.py)  
    - [Populate Next Right Pointer](/algorithms/trees/populate_next_right_pointer.py)  
    - [Postorder](/algorithms/trees/postorder.py)  
    - [Preorder](/algorithms/trees/preorder.py)  
    - [Same Tree](/algorithms/trees/same_tree.py)  
    - [Serialize Tree](/algorithms/trees/serialize_tree.py)  
    - [Sum Of Left Leaves](/algorithms/trees/sum_of_left_leaves.py)  
    - [Sum Root To Leaf Paths](/algorithms/trees/sum_root_to_leaf_paths.py)  
    - [Sum Root To Leafs](/algorithms/trees/sum_root_to_leafs.py)  
    - [Symmetric](/algorithms/trees/symmetric.py)  
    - [Tilt Tree](/algorithms/trees/tilt_tree.py)  
    - [Tree Paths](/algorithms/trees/tree_paths.py)  
    - [Verify Tree Serialization](/algorithms/trees/verify_tree_serialization.py)  
    - [Zigzag Level Order](/algorithms/trees/zigzag_level_order.py)  
  
* [**Trie**](/algorithms/trie)  
    - [*Trie Implementation*](/algorithms/trie/trie_implementation.py)  
    - [Replace Words](/algorithms/trie/replace_words.py)  
  
* [**Two Pointers**](/algorithms/twopointers)  
    - [Container With Most Water](/algorithms/twopointers/container_with_most_water.py)  
    - [Find Duplicate Number](/algorithms/twopointers/find_duplicate_number.py)  
    - [Longest Repeating Character Replacement](/algorithms/twopointers/longest_repeating_character_replacement.py)  
    - [Longest Word In Dictionary](/algorithms/twopointers/longest_word_in_dictionary.py)  
    - [Remove Duplicates](/algorithms/twopointers/remove_duplicates.py)  
    - [Remove Element](/algorithms/twopointers/remove_element.py)  
    - [Three Sum Closest](/algorithms/twopointers/three_sum_closest.py)  
  
