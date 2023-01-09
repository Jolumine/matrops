# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the matrops python package,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from matrops.matrix.Matrix import Matrix
from matrops.exceptions import IncompatibilityException, DifferentSizeException

class MatrixOps: 
    @classmethod
    def check_compatibility(cls, m1:Matrix, m2:Matrix) -> bool:
        if m1.get_number_coloumns() == m2.get_number_rows():
            return True
        else: 
            raise IncompatibilityException("Matrices aren't compatible. m (rows) not equal to n (coloumns)")
        
    @classmethod
    def add(cls, m1:Matrix, m2:Matrix) -> Matrix:
        """
        Adds Matrix 1 and Matrix 2.
        """
        if m1.get_size() == m2.get_size(): 
            result = []
            for zindex in range(m1.get_number_rows()):
                new_row = []
                for sindex in range(m1.get_number_coloumns()):
                    new_row.append(m1.get_data()[zindex][sindex] + m2.get_data()[zindex][sindex])

                result.append(new_row)
            return Matrix(result)
        else: 
            raise DifferentSizeException("Matrices haven't the same size. Size(m1) != Size(m2)")
    
    @classmethod
    def subtract(cls, m1:Matrix, m2:Matrix) -> Matrix:
        """
        Subtracts Matrix 1 from Matrix 2.
        """
        if m1.get_size() == m2.get_size(): 
            result = []
            for zindex in range(m1.get_number_rows()):
                new_row = []
                for sindex in range(m1.get_number_coloumns()):
                    new_row.append(m1.get_data()[zindex][sindex] - m2.get_data()[zindex][sindex])

                result.append(new_row)
            return Matrix(result)  
        else: 
            raise DifferentSizeException("Matrices haven't the same size. Size(m1) != Size(m2)")

    @classmethod
    def multiply(cls, m1:Matrix, m2:Matrix) -> Matrix:
        """
        Multiplys Matrix 1 with Matrix 2
        """
        if cls.check_compatibility(m1, m2): 
            result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*m2.get_data())] for X_row in m1.get_data()]      
            return Matrix(result)

    @classmethod 
    def tranpose(cls, matrix: Matrix) -> Matrix:
        """
        Transposes the matrix. Moves the rows as coloumns.
        """
        result = [[matrix.get_data()[row][coloumn] for row in range(matrix.get_number_rows())] for coloumn in range(matrix.get_number_coloumns())]

        return Matrix(result)