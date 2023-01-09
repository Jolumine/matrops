# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the matrops python package,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

# Module is used to create test data

import random 

def random_number() -> int: 
    """
    Returns a random number beetween -100;100
    """
    return random.randint(-100, 100) # Set range


def main(): 
    rows = 3 # length of row
    coloumns = 3 # number of coloumns

    print([[random_number() for i in range(coloumns)] for j in range(rows)])

if __name__ == "__main__":
    main()
