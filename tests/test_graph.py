from algorithms.graphs import *
import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x 
        self.left = None
        self.right = None 


class TestGraph(unittest.TestCase):
    def test_graph_list(self):
        graph = GraphList()
        graph.add_edge(0, 1) 
        graph.add_edge(0, 4) 
        graph.add_edge(1, 2) 
        graph.add_edge(1, 3) 
        graph.add_edge(1, 4) 
        graph.add_edge(2, 3) 
        graph.add_edge(3, 4) 
        self.assertEqual(graph.bfs(0), [0,1,4,2,3])
        self.assertEqual(graph.dfs(0), [0,1,2,3,4])
        self.assertEqual(graph.dfs_iterative(0), [0,4,3,2,1])

        g = GraphList() 
        g.add_edge(1, 0) 
        g.add_edge(0, 2) 
        g.add_edge(2, 0) 
        g.add_edge(0, 3) 
        g.add_edge(3, 4) 
          
        g1 = GraphList() 
        g1.add_edge(0,1) 
        g1.add_edge(1,2) 
         
        self.assertEqual(g.cycle(), True)
        self.assertEqual(g1.cycle(), False)


        g3 = GraphList()
        g3.add_edge(1,0)  
        g3.add_edge(2,3)  
        g3.add_edge(3,5)
        g3.add_edge(6,9)
        g3.add_edge(7, 7)
        self.assertEqual(g3.count_connected(), 4)
        self.assertEqual(g3.list_connected(), [[0, 1], [2, 3, 5], [6, 9], [7]])
        

        g4 = GraphList()
        g4.add_edge(0,8)
        g4.add_edge(1,5)
        g4.add_edge(1,6)
        g4.add_edge(2,5)
        g4.add_edge(2,7)
        g4.add_edge(3,7)
        g4.add_edge(3,8)
        g4.add_edge(4,7)
    
        self.assertEqual(g4.bipartite(), True)


    def test_graph_matrix(self):

        graph2 = GraphMatrix()
        graph2.add_edge(0, 1) 
        graph2.add_edge(0, 4) 
        graph2.add_edge(1, 2) 
        graph2.add_edge(1, 3) 
        graph2.add_edge(1, 4) 
        graph2.add_edge(2, 3) 
        graph2.add_edge(3, 4) 
        self.assertEqual(graph2.bfs(0), [0,1,4,2,3])
        self.assertEqual(graph2.dfs(0), [0,1,2,3,4])
        g  = GraphMatrix() 
        g.graph = [[-1, 4, -1, -1, -1, -1, -1, 8, -1], 
                   [4, -1, 8, -1, -1, -1, -1, 11, -1], 
                   [-1, 8, -1, 7, -1, 4, -1, -1, 2], 
                   [-1, -1, 7, -1, 9, 14, -1, -1, -1], 
                   [-1, -1, -1, 9, -1, 10, -1, -1, -1], 
                   [-1, -1, 4, 14, 10, -1, 2, -1, -1], 
                   [-1, -1, -1, -1, -1, 2, -1, 1, 6], 
                   [8, 11, -1, -1, -1, -1, 1, -1, 7], 
                   [-1, -1, 2, -1, -1, -1, 6, 7, -1] 
                  ]; 

        self.assertEqual(g.print_shortest_paths(0), [[0, 1], [0, 1, 2], [0, 1, 2, 3], 
                                                     [0, 7, 6, 5, 4], [0, 7, 6, 5], [0, 7, 6], [0, 7], 
                                                     [0, 1, 2, 8]])

class TestGraphFunctions(unittest.TestCase):
    def test_word_ladder(self):
        self.assertEqual(word_ladder('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']), 0)
        self.assertEqual(word_ladder('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']), 0)
        self.assertEqual(word_ladder_v2('hit', 'cog', ["hot","dot","dog","lot","log","cog"]), 5)
        self.assertEqual(word_ladder_v2('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']), 0)

    def test_word_ladder_two(self):
        self.assertEqual(len(word_ladder_two('hit', 'cog', ["hot","dot","dog","lot","log","cog"])), 2)

    def test_is_bipartate(self):
        self.assertEqual(is_bipartate([[1,3], [0,2], [1,3], [0,2]]), True)
        self.assertEqual(is_bipartate([[1,2,3], [0,2], [0,1,3], [0,2]]), False)
        self.assertEqual(is_bipartate([[], [2,4,6],[1,4,8,9],[7,8],[],[1,2,8,9],[6,9],[1,5,7,8,9],
                                      [3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]), False)
        self.assertEqual(is_bipartate([[]]), True)

    def test_surround(self):
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        self.assertEqual(surround(board), [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], 
                                           ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']])

    def test_number_islands(self):
        self.assertEqual(number_islands([["1","1","1","1","0"],["1","1","0","1","0"],
                                        ["1","1","0","0","0"],["0","0","0","0","0"]]), 1)

    def test_right_side(self):
        class Node:
            def __init__(self, x):
                self.data = x
                self.left = None
                self.right = None

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.right = Node(5)
        root.right.right = Node(4)

        self.assertEqual(right_side(root), [1,3,4])
        self.assertEqual(right_side_v2(root), [1,3,4])

    def test_course_order(self):
        self.assertEqual(course_order(2, [[1, 0]]), True)
        self.assertEqual(course_order(2, [[1, 0], [0,1]]), False)

    def test_word_search(self):
        board = [
                  ['A','B','C','E'],
                  ['S','F','C','S'],
                  ['A','D','E','E']
                ]
        self.assertEqual(word_search(board, 'ABCCED'), True)
        self.assertEqual(word_search(board, 'SEE'), True)
        self.assertEqual(word_search(board, 'ABCB'), False)

    def test_jump_game_two(self):
        self.assertEqual(jump_game_two([2,3,1,1,4]), 2)

    def test_house_robber(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(1)
        self.assertEqual(rob(root), 7)

    def test_pacific(self):
        matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        self.assertEqual(len(pacific_atlantic(matrix)), 7)

    def test_concatenated_words(self):
        self.assertEqual(concatenated_words(["cat","cats","catsdogcats","dog","dogcatsdog",
                                             "hippopotamuses","rat","ratcatdogcat"]), 
                                             ["catsdogcats","dogcatsdog","ratcatdogcat"])
    
    def test_mine(self):
        board =  [['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'M', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E']]

        result = [['B', '1', 'E', '1', 'B'],
                 ['B', '1', 'M', '1', 'B'],
                 ['B', '1', '1', '1', 'B'],
                 ['B', 'B', 'B', 'B', 'B']]

        self.assertEqual(minesweeper(board, [3,0]), result)

    def test_max_area_islands(self):
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]

        grid2 = [[0,0,0,0,0,0,0,0]]
        self.assertEqual(max_area_island(grid), 6)
        self.assertEqual(max_area_island(grid2), 0)

    def test_friends(self):
        grid =  [[1,1,0],
                 [1,1,0],
                 [0,0,1]]
        self.assertEqual(friend_circle(grid), 2)

    def test_get_imp(self):
        employees = list()
        e1 = Employee(1,2,[2])
        e2 = Employee(2,3,[])
        employees.append(e1)
        employees.append(e2)
        self.assertEqual(get_importance(employees, 2), 3)

    def test_flood_fill(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        result = [[2,2,2],[2,2,0],[2,0,1]]

        self.assertEqual(flood_fill(image, 1, 1, 2), result)

    def test_oranges(self):
        self.assertEqual(orange([[2,1,1],[1,1,0],[0,1,1]]), 4)

    def test_make_larger_island(self):
        grid = [[1, 0], [0, 1]]
        self.assertEqual(largest_island(grid), 3)
        self.assertEqual(largest_island([[1, 1], [1, 1]]), 4)

    def test_min_height_trees(self):
        self.assertEqual(find_min_height_trees(4, [[1,0],[1,2],[1,3]]), [1])

    def test_network_delay_time(self):
        self.assertEqual(network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2), 2)


    def test_town_judge(self):
        self.assertEqual(find_judge(2, [[1,2]]), 2)

    def test_keys_rooms(self):
        self.assertEqual(keys_and_rooms([[1],[2],[3],[]]), True)

    def test_flowers_plant(self):
        self.assertEqual(flower_planting(4, [[1,2],[3,4]]), [1,2,1,2])
        
if __name__ == '__main__':
    unittest.main()
