# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the matrops python package,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import unittest

from matrops.matrix import Matrix as M, MatrixOps

class TestMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.test_matrix1 = M([[9, 78, 62, 85], [15, 87, 57, 4], [79, 47, 15, 70], [35, 55, 82, 23]])
        self.test_matrix2 = M([[21, 96, 27, 82], [97, 44, 36, 31], [78, 43, 53, 57], [63, 11, 37, 42]])

        self.test_matrix3 = M([[-24, -27, -22, 100], [47, -56, -12, 51], [-4, -55, -92, -58], [36, 54, 17, -6]])
        self.test_matrix4 = M([[-19, 90, -25, 71], [-4, 11, 78, -66], [-93, 83, -48, -23], [2, 85, -58, 82]])

        self.test_matrix5 = M([[4, 9, 9], [9, 1, 6], [9, 2, 3]])
        self.test_matrix6 = M([[2, 2], [5, 7], [4, 4]])

    def test_addition(self) -> None: 
        result = MatrixOps.add(self.test_matrix3, self.test_matrix4).get_data()
        real_result = [[-43, 63, -47, 171], [43, -45, 66, -15], [-97, 28, -140, -81], [38, 139, -41, 76]]
        self.assertEqual(result, real_result)

    def test_subtraction(self) -> None: 
        result = MatrixOps.subtract(self.test_matrix1, self.test_matrix2).get_data()
        real_result = [[-12, -18, 35, 3], [-82, 43, 21, -27], [1, 4, -38, 13], [-28, 44, 45, -19]]
        self.assertEqual(result, real_result)

    def test_multiplication(self) -> None:
        result = MatrixOps.multiply(self.test_matrix5, self.test_matrix6).get_data()
        real_result = [[89, 107], [47,  49], [40,  44]]
        self.assertEqual(result, real_result)

    def test_scale(self) -> None: 
        result = self.test_matrix6.scale(2).get_data()
        real_result = [[4, 4], [10, 14], [8, 8]]
        self.assertEqual(result, real_result)

    def test_transpose(self) -> None: 
        result = MatrixOps.tranpose(self.test_matrix6).get_data()
        real_result = [[2, 5, 4], [2, 7, 4]]
        self.assertEqual(result, real_result) 