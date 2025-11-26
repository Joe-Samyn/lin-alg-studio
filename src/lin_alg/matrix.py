
"""
TODO: Figure out how to make size readonly. If the matrix size needs to be changed, a new matrix will need to be created. 
TODO: Change properties from `n` and `m` to `rows` and `columns`
"""


class Matrix: 
    """An two dimensional array of numbers with dimensions M x N, where M is the number
    of rows and N is the number of columns. 
    """

    def __init__(self, matrix: list[list] = None, m: int = 0, n: int = 0):
        """Initialize an M x N matrix.
    
        If `matrix` is provided, dimensions are determined from the matrix size.
        Otherwise, a zero-filled matrix is created using `rows` and `columns`.
        
        Parameters
        ----------
        matrix : list[list[float]] | list[list[int]], optional
            A 2D array of numbers. If rows have inconsistent lengths, shorter rows 
            are padded with zeros to match the longest row. Default is [[]].
        m : int, optional
            Number of rows for the matrix when `matrix` is not provided. Default is 0.
        n : int, optional
            Number of columns for the matrix when `matrix` is not provided. Default is 0.
        """
        if matrix is not None:
            self.n = 0
            # Determine longest row 
            for row in matrix:
                if self.n < len(row):
                    self.n = len(row)
            
            # Pad rows as needed 
            for row in matrix:
                if len(row) < self.n:
                    delta = self.n - len(row)
                    row.extend([0] * delta)
        
            self.data = matrix 
            self.m = len(matrix)

        elif matrix is None:
            self.data = [[0] * n for _ in range(m)] 
            self.m = m
            self.n = n
    
    def __getitem__(self, indices):
        """NOTE: The slicing operation currently only supports [:, col_index]. This allows an entire column to be retrieved.
        There will be future enhancements to implement full slicing functionality.
        """
        # Accessing entire row
        if isinstance(indices, int):
            return self.data[indices]
        
        # Accessing element
        elif isinstance(indices, tuple):
            row, col = indices

            # Accessing slice of row or full column
            if isinstance(row, slice):
                column_vector = []
                for row_vector in self.data:
                    column_vector.append(row_vector[col])
                return column_vector
            else:
                return self.data[row][col]
        else:
            # TODO: may want to error? 
            pass

    def __setitem__(self, indicies, value):
        """NOTE: The current splicing syntax only supports editing a single element at a time.
        There will be future enhancements to support full row and column updates.
        """
        if isinstance(indicies, tuple):
            row, col = indicies
            self.data[row][col] = value
        else:
            # TODO: May want to raise error
            pass

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Adds two matrices, A (m x n) and B (m x n) together.
        
        Parameters
        ----------
        other: Matrix
            The matrix to add.
            
        Returns
        -------
        Matrix
            A new instance of Matrix whose elements are the sum of corresponding elements in A & B.
            
        Raises
        ------
        ValueError
            If self.m != other.m or self.n != other.n (i.e. dimension of A != dimension of B)

        Notes
        -----
        Complexity: O(m * n)
            
        Examples
        --------
        >>> A = Matrix([[1, 2],[3, 4]])
        >>> B = Matrix([[3, 4],[5, 6]])

        >>> C = A + B  # results in 2x2
        >>> C.data
        [[4, 6], [8, 10]]

        """
        if self.m != other.m or self.n != other.n:
            raise ValueError("Matrices must be the same dimensions when performing matrix addition.")
        
        sum_matrix = Matrix(m=self.m, n=self.n)

        for row in range(0, self.m):
            for col in range(0, self.n):
                sum_matrix[row,col] = self[row,col] + other[row,col]
        return sum_matrix
    
    # TODO: Much more optimal ways to perform matrix multiplication
    def __mul__(self, other: 'Matrix') -> 'Matrix':
        """Multiplies two matrices, A (m x n) and B (n x k). 

        The number of columns in A (n) must equal the number of rows in B (n). 

            A     *    B    =     C
         (m x n)    (n x k)    (m x k)

        Parameters
        ----------
        other: Matrix
            The 'B' matrix with dimensions (n x k).

        Returns
        -------
        Matrix
            A new instance of an (m x k) matrix that is the product of A * B. 

        Raises
        -------
        ValueError
            If self.n != other.m (i.e. columns of A != rows of B) 

        Notes
        ------
        Performance will be optimized in a future release. 
        Complexity: O(m * n * k) 
        
        Examples
        --------
        >>> A = Matrix([[1, 2], [3, 4]])
        >>> B = Matrix([[3, 4], [4, 5]])
        >>> C = A * B   # Result is a 2x2 square matrix
        >>> C.data
        [[11, 14], [25, 32]]

        """
        # Columns of self need to match rows of other
        if self.n != other.m:
            raise ValueError("The dimensions of the matrices do not align properly for matrix multiplication.")

        C = Matrix(m=self.m, n=other.n)
        for r in range(0, self.m):
            row = self.data[r]
            # Have row in A 
            for c in range(0, other.n):
                col = other[:,c]
                element = 0
                for i in range(0, len(row)):
                    element += row[i] * col[i]
                
                C[r, c] = element

        return C
        


    @staticmethod
    def identity(size: int) -> "Matrix":
        """Creates a square MxM identity matrix.
        Parameters
        ----------
        size : int
            The size of the square identity matrix (number of rows / columns).
            Must be greater than 0. 
        
        Returns
        -------
        Matrix
            An instance of an MxM identity matrix

        Raises
        ------
        ValueError 
            if m is not greater than 0. 
        
        Examples
        --------
        >>> Matrix.identity(3)
        [[1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]]
        """
        if size <= 0:
            raise ValueError("`m` mus be greater than 0.")
        
        idm = Matrix(m=size, n=size)
        for i in range(0, size): 
            idm.data[i][i] = 1
        return idm
