# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the matrops python package,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from matrops.vector.Vector import Vector
from matrops.exceptions import IncompatibilityException


class VectorOps:
    @classmethod
    def check_compatibilty(self, v1:Vector, v2:Vector) -> bool: 
        if v1.get_dimensions() == v2.get_dimensions(): 
            return True
        else: 
            raise IncompatibilityException(f"Vectors don't have the same dimension. {v1.get_dimensions()} != {v2.get_dimensions()}")
    
    @classmethod
    def add(cls, v1:Vector, v2:Vector) -> Vector: 
        if cls.check_compatibilty(v1, v2):
            result = []
            for index in range(v1.get_dimensions()): 
                result.append(v1.get_data()[index]+v2.get_data()[index])
            
            return Vector(result)

    @classmethod
    def subtract(cls, v1:Vector, v2:Vector) -> Vector: 
        if cls.check_compatibilty(v1, v2):
            result = []
            for index in range(v1.get_dimensions()): 
                result.append(v1.get_data()[index]-v2.get_data()[index])
            
            return Vector(result) 

    @classmethod
    def multiply(cls, v1:Vector, v2:Vector) -> Vector:
        if cls.check_compatibilty(v1, v2):
            result = []
            for index in range(v1.get_dimensions()): 
                result.append(v1.get_data()[index]*v2.get_data()[index])
            
            return Vector(result) 
