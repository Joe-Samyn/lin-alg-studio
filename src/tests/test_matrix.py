import unittest 
from src.lin_alg.matrix import Matrix

class TestMatrix(unittest.TestCase):

    def test_createMatrixWithRowsAndColumns_CreatesMatrixOfProperSize(self):
        # Arrange
        rows = 5
        cols = 5
        expList = [[0] * cols] * rows 

        # Act
        m = Matrix(m=rows, n=cols)
        
        # Assert
        self.assertEqual(expList, m.data)
        

    def test_createMatrixWithMatrix_CreatesMatrix(self):
        # Arrange
        exp = [[0] * 5] * 5

        # Act
        m = Matrix(matrix=exp)

        # Assert
        self.assertEqual(m.data, exp)

    def test_createMatrixWithDifferentSizeRows_PadsAllRowsToLongest(self):
        # Arrange
        exp_col_size = 5
        l = [
            [1, 2, 3],
            [1, 2, 3, 4, 5],
            [1, 3]
        ]

        # Act
        m = Matrix(matrix=l)
        row_one_size =len(m.data[0])
        row_two_size = len(m.data[1])
        row_three_size = len(m.data[2])

        # Assert
        self.assertEqual(row_one_size, exp_col_size)
        self.assertEqual(row_two_size, exp_col_size)
        self.assertEqual(row_three_size, exp_col_size)

    def test_matrixElementAccess_returnsSingleElement(self):
        # Arrange
        matrix = Matrix(matrix=[[1, 2, 3], [4, 5, 6]])
        exp = 2

        # Act
        res = matrix[0, 1]

        # Assert
        self.assertEqual(res, exp)
    
    def test_matrixRowAccess_returnsEntireRow(self):
        # Arrange
        matrix = Matrix(matrix=[[1, 2, 3], [4, 5, 6]])
        exp = [1, 2, 3]

        # Act
        res = matrix[0]

        # Assert
        self.assertEqual(exp, res)
    
    def test_matrixColumnAccess_returnsEntireColumn(self):
        # Arrange
        matrix = Matrix(matrix=[[1, 2, 3], [4, 5, 6]])
        exp = [2, 5]

        # Act
        res = matrix[:, 1]

        # Assert
        self.assertEqual(res, exp)

    def test_matrixAddition_returnsNewSumMatrix(self):
        # Arrange
        exp = Matrix(matrix=[
            [6, 8],
            [10, 12]
        ])
        A = Matrix(matrix=[
            [1, 2],
            [3, 4]
        ])

        B = Matrix(matrix=[
            [5, 6],
            [7, 8]
        ])

        # Act
        result = A + B

        # Assert
        self.assertEqual(result[0,0], exp[0,0])
        self.assertEqual(result[0,1], exp[0,1])
        self.assertEqual(result[1,0], exp[1,0])
        self.assertEqual(result[1,1], exp[1,1])

    def test_matrixAddition_raisesErrorWhenMatricesDifferentDimensions(self):
        # Arrange
        A = Matrix(matrix=[
            [1, 2],
            [3, 4]
        ])

        B = Matrix(matrix=[
            [5, 6],
            [7, 8],
            [8, 9]
        ])

        # Act & Assert
        with self.assertRaises(ValueError):
            A + B
