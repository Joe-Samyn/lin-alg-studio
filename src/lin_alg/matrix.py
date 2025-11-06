from typing import List

class Matrix: 

    # TODO: This needs to look at the arguments and perform the proper initialization based on what was
    # provided
    def __init__(self, matrix: List[List] = [[]], rows: int = 0, columns: int = 0):
        self.m = [[0] * columns] * rows
        self.rows = rows
        self.columns = columns


