import unittest


from solver import Board, SudokuSolver


class TestSum(unittest.TestCase):
    def test_easy(self):
        b = Board([
            [1, 0, 6, 0, 0, 2, 3, 0, 0],
            [0, 5, 0, 0, 0, 6, 0, 9, 1],
            [0, 0, 9, 5, 0, 1, 4, 6, 2],
            [0, 3, 7, 9, 0, 5, 0, 0, 0],
            [5, 8, 1, 0, 2, 7, 9, 0, 0],
            [0, 0, 0, 4, 0, 8, 1, 5, 7],
            [0, 0, 0, 2, 6, 0, 5, 4, 0],
            [0, 0, 4, 1, 5, 0, 6, 0, 9],
            [9, 0, 0, 8, 7, 4, 2, 1, 0],
        ])
        self.assertEqual(repr(SudokuSolver.solve(b)), repr([[1, 4, 6, 7, 9, 2, 3, 8, 5], [2, 5, 8, 3, 4, 6, 7, 9, 1], [3, 7, 9, 5, 8, 1, 4, 6, 2], [4, 3, 7, 9, 1, 5, 8, 2, 6], [
            5, 8, 1, 6, 2, 7, 9, 3, 4], [6, 9, 2, 4, 3, 8, 1, 5, 7], [7, 1, 3, 2, 6, 9, 5, 4, 8], [8, 2, 4, 1, 5, 3, 6, 7, 9], [9, 6, 5, 8, 7, 4, 2, 1, 3]]), "Wrong answer")

    def test_hard(self):
        b = Board([
            [4, 0, 9, 3, 7, 0, 0, 0, 0],
            [1, 0, 0, 4, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 9, 0, 1, 0],
            [5, 0, 0, 0, 0, 6, 0, 7, 0],
            [0, 6, 2, 0, 0, 0, 5, 8, 0],
            [0, 1, 0, 2, 0, 0, 0, 0, 3],
            [0, 2, 0, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 2, 0, 0, 8],
            [0, 0, 0, 0, 9, 7, 6, 0, 5],
        ])
        self.assertEqual(repr(SudokuSolver.solve(b)), repr([[4, 8, 9, 3, 7, 1, 2, 5, 6], [1, 5, 6, 4, 2, 8, 9, 3, 7], [2, 7, 3, 5, 6, 9, 8, 1, 4], [5, 4, 8, 9, 3, 6, 1, 7, 2], [
            3, 6, 2, 7, 1, 4, 5, 8, 9], [9, 1, 7, 2, 8, 5, 4, 6, 3], [6, 2, 5, 8, 4, 3, 7, 9, 1], [7, 9, 1, 6, 5, 2, 3, 4, 8], [8, 3, 4, 1, 9, 7, 6, 2, 5]]), "Wrong answer")

    def test_empty(self):
        b = Board([
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])
        self.assertEqual(repr(SudokuSolver.solve(b)), repr([[1, 2, 3, 4, 5, 8, 9, 6, 7], [4, 5, 8, 6, 7, 9, 1, 2, 3], [9, 6, 7, 1, 2, 3, 8, 4, 5], [2, 1, 9, 8, 3, 4, 5, 7, 6], [
            3, 8, 4, 5, 6, 7, 2, 1, 9], [5, 7, 6, 9, 1, 2, 3, 8, 4], [8, 9, 1, 3, 4, 6, 7, 5, 2], [6, 3, 2, 7, 8, 5, 4, 9, 1], [7, 4, 5, 2, 9, 1, 6, 3, 8]]), "Wrong answer")


if __name__ == '__main__':
    unittest.main()
