```
                                    _                       
                                    | |                      
                    _ __ ___   __ _| |_ _ __ ___  _ __  ___ 
                    | '_ ` _ \ / _` | __| '__/ _ \| '_ \/ __|
                    | | | | | | (_| | |_| | | (_) | |_) \__ \
                    |_| |_| |_|\__,_|\__|_|  \___/| .__/|___/
                                                | |        
                                                |_|        
```

# :1234: Matrops

This is a python package for matrix and vector operations like, addition, substraction, multiplication, scale and transpose. <br>
More options like graphics for vectors, calculating the angle beetween to vectors and more are comming soon. 
<br>

## :scroll: Table of contents 

- Installation 
- Example
- Coming soon
- Contributors

<br>

## :white_check_mark: Installation 

```ps
git clone <link>
cd matrops/
python setup.py install
```

```ps
python -m matrops
```

<br>

## :arrow_forward: Example

```py
from matrops.matrix import Matrix, MatrixOps

# create 2 matrices
matrix_1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
matrix_2 = Matrix([[2, 2, 2, 2], [3, 3, 3, 3]])

if __name__ == "__main__":
    # Add 2 matrices 
    added = MatrixOps.add(matrix_1, matrix_2)

    # Scale matrix with 2
    matrix_1.scale(2)

    # Transpose matrix 
    transposed = MatrixOps.tranpose(matrix_1)

    # Read documentation for more usage examples 
```
<br>

## :soon: Coming soon 

- Detailed calculations
- Possibility to calculate the angle beetween 2 vectors
- Show vectors in a graphical interface

<br>


## :busts_in_silhouette: Contributors

- Leonard Becker