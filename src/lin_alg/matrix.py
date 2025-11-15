

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
        # TODO: Do we need to validate any of the parameters here? 
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
            self.data = [[0] * n] * m
            self.m = m
            self.n = n

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
        # TODO: Diagonal needs to be 1's
        if size <= 0:
            raise ValueError("`m` mus be greater than 0.")
        return Matrix(m=size, n=size)
