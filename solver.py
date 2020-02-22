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
        self.board = [[Cell(self, i, j, value)
                       for (j, value) in enumerate(row)] for (i, row) in enumerate(board)]

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
            board_map = {}
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
