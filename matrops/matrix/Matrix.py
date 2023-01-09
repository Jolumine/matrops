# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the matrops python package,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from matrops.matrix import Matrix
from matrops.exceptions import NoMatrixException, DifferentSizeException

class Matrix: 
    def __init__(self, data:list[list]) -> None: 
        for index, row in enumerate(data): 
            if type(row) != list: 
                raise NoMatrixException(f"Input is not a matrix, row {index+1} is not an array.")
            else: 
                continue

        self.__data = data
        self.__number_rows = len(self.__data)
        self.__number_coloumns = len(self.__data[0])

    
    def scale(self, scalar:int) -> Matrix: 
        """
        Multiplys the matrix with the scalar. 
        """
        for rindex in range(self.__number_rows):
            for cindex in range(self.__number_coloumns):
                self.__data[rindex][cindex]*=scalar

        return self


    def print(self) -> None:
        """
        Prints the data contained by the matrix
        """
        for rindex in range(self.__number_rows):
            for cindex in range(self.__number_coloumns): 
                print(f"x({rindex+1},{cindex+1}) = {self.__data[rindex][cindex]}", end="\t")
            print() 

    def get_data(self) -> list[list]:
        """
        Returns the containing data
        """
        return self.__data

    def get_size(self) -> tuple: 
        """
        Returns the size of the matrix
        """
        return (self.__number_coloumns, self.__number_rows)

    def get_number_rows(self) -> int:
        """
        Returns the number of rows
        """
        return self.__number_rows

    def get_number_coloumns(self) -> int:
        """
        Returns the number of coloumns
        """
        return self.__number_coloumns

