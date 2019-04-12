from algorithms.matrix import *
import unittest 

class TestSuite(unittest.TestCase):
    def test_rotate_image(self):
        self.assertEqual(rotate_image([[1,2,3],[4,5,6],[7,8,9]]),
                                      [[7,4,1],[8,5,2],[9,6,3]])
        self.assertEqual(rotate_image([[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]),
                                      [[15,13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7,10,11]])

    def test_spiral_matrix(self):
        self.assertEqual(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(spiral_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])

    def test_generate_matrix(self):
        self.assertEqual(generate_spiral_matrix(3), [[1,2,3],[8,9,4],[7,6,5]])
        self.assertEqual(generate_spiral_matrix(1), [[1]])
        self.assertEqual(generate_spiral_matrix(0), [])
        self.assertEqual(generate_spiral_matrix(2), [[1,2],[4,3]])

    def test_matrix_reshape(self):
        self.assertEqual(reshape_matrix([[1,2],[3,4]],1,4),[[1,2,3,4]])

    def test_matrix_zeros(self):
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        self.assertEqual(set_matrix_zeros(matrix), [[1,0,1],[0,0,0],[1,0,1]])
    
    def test_island_perimeter(self):
        matrix = [[0,1,0,0],
                 [1,1,1,0],
                 [0,1,0,0],
                 [1,1,0,0]]

        self.assertEqual(island_perimeter(matrix), 16)

    def test_image_smoother(self):
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        output = [[0,0,0],[0,0,0],[0,0,0]]

        self.assertEqual(image_smoother(matrix), output)