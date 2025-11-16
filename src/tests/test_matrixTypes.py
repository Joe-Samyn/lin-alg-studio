
import unittest
from lin_alg.matrix import Matrix

class TestMatrixTypes(unittest.TestCase):


    def test_createIdentityMatrix_returnsIdentityMatrixWithProperSize(self):
        # Arrange
        exp = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        size = 3

        # Act
        res = Matrix.identity(size=size).data

        # Assert
        self.assertEqual(res, exp)
