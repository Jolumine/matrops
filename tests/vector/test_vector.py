# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the matrops python package,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import unittest

from matrops.vector import Vector as V, VectorOps

class TestVector(unittest.TestCase):
    def setUp(self):
        self.test_vector1 =  V([3, 3, 3])
        self.test_vector2 = V([1, 1, 1])
        self.test_vector3 = V([4, 7, 2])
        self.test_vector4 = V([12, 32, 2])
        self.test_vector5 = V([3, 1])
        self.test_vector6 = V([10, 21])
    
    def test_addition(self) -> None: 
        result1 = VectorOps.add(self.test_vector1, self.test_vector2).get_data()
        real_result1 = [4, 4, 4]
        result2 = VectorOps.add(self.test_vector3, self.test_vector4).get_data()
        real_result2 = [16, 39, 4]
        self.assertEqual(result1, real_result1)
        self.assertEqual(result2, real_result2)

    def test_scale(self) -> None:
        result = self.test_vector4.scale(3).get_data()
        real_result = [36, 96, 6]
        self.assertEqual(result, real_result)

    def test_subtraction(self) -> None:
        result = VectorOps.subtract(self.test_vector4, self.test_vector3).get_data()
        real_result = [8, 25, 0]
        self.assertEqual(result, real_result)

    def test_multiplication(self) -> None:
        result = VectorOps.multiply(self.test_vector1, self.test_vector3).get_data()
        real_result = [12, 21, 6] 
        self.assertEqual(result, real_result)


    
        