import unittest 
from src.lin_alg.matrix import Matrix

class TestMatrix(unittest.TestCase):

    def test_createMatrixWithRowsAndColumns_CreatesMatrixOfProperSize(self):
        # Arrange
        rows = 5
        cols = 5
        expList = [[0] * cols] * rows 

        # Act
        m = Matrix(rows=rows, columns=cols)
        
        # Assert
        self.assertEqual(expList, m.m)
        

    def test_createMatrixWithMatrix_CreatesMatrix(self):
        # Arrange
        exp = [[0] * 5] * 5

        # Act
        m = Matrix(matrix=exp)

        # Assert
        self.assertEqual(m, exp)