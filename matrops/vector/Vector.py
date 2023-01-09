# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the matrops python package,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from matrops.vector import Vector
from matrops.exceptions import VectorUsageException

class Vector:
    def __init__(self, data):
        if len(data) >= 2 and type(data[0]) != list: 
            self.__data = data
        else: 
            raise VectorUsageException("More than 1 coloumn. Use Matrix.")

        self.__length = len(self.__data)

    def print(self, title="") -> None:
        """
        Prints the vector
        """
        if title != "": 
            sep = ""
            length = len(title)
            for i in range(length): 
                sep+="-"
            print(title)
            print(sep)
            for element in self.__data: 
                print(f"{element}")
            print(sep)
        else: 
            print("-------")
            for element in self.__data: 
                print(f"{element}")
            print("-------")

    def scale(self, scalar:int) -> Vector: 
        """
        Multiplys the vector with the scalar
        """
        for index in range(self.__length):
            self.__data[index] *= scalar

        return self

    def get_length(self) -> int: 
        """
        Returns the geometrical length of the vector
        (Prepared for angle calculations)
        """
        result = 0
        for number in self.__data: 
            result+=number**2
        
        return round(result**0.5)

    def get_dimensions(self) -> int: 
        """
        Returns the length
        """
        return self.__length

    def get_data(self) -> list: 
        """
        Returns the containing data
        """
        return self.__data
