# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the matrops python package,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

class VectorUsageException(Exception):
    def __init__(self, error:str) -> None:
        return super().__init__(error)

class IncompatibilityException(Exception):
    def __init__(self, error) -> None:
        return super().__init__(error)
    
class NoMatrixException(Exception):
    def __init__(self, error:str) -> None: 
        return super().__init__(error)
        
class DifferentSizeException(Exception):
    def __init__(self, error:str) -> None: 
        return super().__init__(error)