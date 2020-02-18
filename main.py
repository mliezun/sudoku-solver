# SudokuSolver


class Cell:
    def __init__(self, b, i, j, value):
        self.b = b
        self.value = value
        self.i = i
        self.j = j

    def options(self):
        if self.value != 0:
            return {self.value}
        options = set(range(1, 10))
        row = set(map(lambda x: x.value, self.b[self.i]))
        column = set(map(lambda x: x.value, self.b[:][self.j]))
        def to_square(k): return slice((k // 3) * 3, (k // 3) * 3 + 3)
        square = set(
            map(lambda x: x.value,
                self.b[to_square(self.i)][to_square(self.j)]))
        return options - row - column - square - {0}

    def __repr__(self):
        return repr(self.value)


class BoardSlice:
    def __init__(self, board_slice):
        self.board_slice = board_slice

    def __getitem__(self, items):
        if type(items) == slice:
            return (el for row in self.board_slice for el in row[items])
        if type(items) == int:
            return (row[items] for row in self.board_slice)
        raise KeyError


class Board:
    def __init__(self, board):
        self.board = []
        for (i, row) in enumerate(board):
            cells = []
            for (j, value) in enumerate(row):
                cells.append(Cell(self, i, j, value))
            self.board.append(cells)

    def copy(self):
        return Board(((cell.value for cell in row) for row in self.board))

    def __getitem__(self, items):
        if type(items) == int:
            return self.board[items]
        if type(items) == slice:
            return BoardSlice(self.board[items])
        raise KeyError

    def __repr__(self):
        return repr(self.board)


class SudokuSolver:
    @staticmethod
    def solve(board):
        b = board.copy()
        # First pass: Iterative
        board_map = {}
        exhaust = False
        while not exhaust:
            exhaust = True
            for i in range(9):
                for j in range(9):
                    cell = b[i][j]
                    if cell.value == 0:
                        options = cell.options()
                        if len(options) == 1:
                            cell.value = options.pop()
                            exhaust = False
                        elif len(options) == 0:
                            return None
                        elif len(board_map) == 0:
                            board_map[(i, j)] = options

        # Second pass: Recursive
        for ((i, j), options) in board_map.items():
            for op in options:
                b[i][j].value = op
                solved = SudokuSolver.solve(b)
                if solved:
                    return solved
            return None

        return b


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
assert SudokuSolver.solve(b).__repr__() == [[1, 4, 6, 7, 9, 2, 3, 8, 5], [2, 5, 8, 3, 4, 6, 7, 9, 1], [3, 7, 9, 5, 8, 1, 4, 6, 2], [4, 3, 7, 9, 1, 5, 8, 2, 6], [
    5, 8, 1, 6, 2, 7, 9, 3, 4], [6, 9, 2, 4, 3, 8, 1, 5, 7], [7, 1, 3, 2, 6, 9, 5, 4, 8], [8, 2, 4, 1, 5, 3, 6, 7, 9], [9, 6, 5, 8, 7, 4, 2, 1, 3]].__repr__()


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
assert SudokuSolver.solve(b).__repr__() == [[4, 8, 9, 3, 7, 1, 2, 5, 6], [1, 5, 6, 4, 2, 8, 9, 3, 7], [2, 7, 3, 5, 6, 9, 8, 1, 4], [5, 4, 8, 9, 3, 6, 1, 7, 2], [
    3, 6, 2, 7, 1, 4, 5, 8, 9], [9, 1, 7, 2, 8, 5, 4, 6, 3], [6, 2, 5, 8, 4, 3, 7, 9, 1], [7, 9, 1, 6, 5, 2, 3, 4, 8], [8, 3, 4, 1, 9, 7, 6, 2, 5]].__repr__()


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
assert SudokuSolver.solve(b).__repr__() == [[1, 2, 3, 4, 5, 8, 9, 6, 7], [4, 5, 8, 6, 7, 9, 1, 2, 3], [9, 6, 7, 1, 2, 3, 8, 4, 5], [2, 1, 9, 8, 3, 4, 5, 7, 6], [
    3, 8, 4, 5, 6, 7, 2, 1, 9], [5, 7, 6, 9, 1, 2, 3, 8, 4], [8, 9, 1, 3, 4, 6, 7, 5, 2], [6, 3, 2, 7, 8, 5, 4, 9, 1], [7, 4, 5, 2, 9, 1, 6, 3, 8]].__repr__()
