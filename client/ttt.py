from noughtsandcrosses import InvalidMoveException

class TTT(object):
    def __init__(self, size, piece, evaluator):
        """
        Initializes the board with size = size * size (row x col) and indicates that
        the first to move is player 'piece'
        :param size: size of board
        :param piece: which player starts first (x or o)
        :param evaluator: Evaluator class to be used for evaluating boards
        """
        self.state = TTT.Board(size)
        self.piece = piece.lower()

    def update(self, action):
        """
        apply action *in-place* on the board itself
        """
        self.state.update(action, self._get_player_this_move())

    def apply_action(self, action):
        """
        returns the new board after action is applied on a copy of the current board,
        the current board is not changed
        """
        copy_ttt = self.clone()
        copy_ttt.state.update(action, self._get_player_this_move())
        return copy_ttt

    def get_actions(self):
        return [(index + 1) for index, pos in enumerate(self.state.brd) if pos == TTT.Board.BLANK]

    def evaluate(self):
        self.evaluator.evaluate(self.board)

    def is_terminal(self):
        return self.state.draw() or self.state.get_winner() != None


    def clone(self):
        """
        returns a deep copy of this TTT state
        """
        # create a new copy of TTT
        new_copy = TTT(self.state.size, self.piece)
        # override the empty board
        new_copy.state.brd = list(self.state.brd)
        return new_copy

    def _get_player_this_move(self):
        """
        returns who should make a move this round
        defaults to the first player if number of pieces are even on the board
        """
        num_x = self.state.brd.count(TTT.Board.X)
        num_o = self.state.brd.count(TTT.Board.O)
        if num_x == num_o:
            return self.piece
        return TTT.Board.X if num_o > num_x else TTT.Board.O

    class Board(object):
        BLANK, X, O = " ", "x", "o"
        def __init__(self, size):
            self.size = size
            self.brd = [TTT.Board.BLANK]*(size*size)

        def update(self, move, piece):
            """
            updates the internal board in-place
            """
            if move == None:
                return
            if self.brd[move-1] != TTT.Board.BLANK:
                raise InvalidMoveException("Placing a piece on occupied position {} ".format(move) + \
                     "on board but piece {} already occupied position\n".format(self.brd[move-1]) + self.__str__())
            self.brd[move-1] = piece

        def get_winner(self):
            """
            returns the winner's symbol, None otherwise
            """
            # check diagonals
            # \ diagonal
            all_diagonals = get_diagonals(self.board)
            diag1 = all_diagonals[0]

            if TTT.Board._all_same(diag1) and diag1[0] != TTT.Board.BLANK:
                return diag1[0]

            # / diagonal
            diag2 = all_diagonals[1]
            if TTT.Board._all_same(diag2) and diag2[0] != TTT.Board.BLANK:
                return diag2[0]

            # check rows and cols
            for i in range(self.size):
                row = self.brd[i*self.size:(i+1)*self.size]
                if TTT.Board._all_same(row) and row[0] != TTT.Board.BLANK:
                    return row[0]
                col = [self.brd[i+(self.size*j)] for j in range(self.size)]
                if TTT.Board._all_same(col) and col[0] != TTT.Board.BLANK:
                    return col[0]
            return None

        def draw(self):
            """
            :returns: true if it's a draw game
            """
            return self.brd.count(TTT.Board.BLANK) == 0

        @staticmethod
        def _all_same(iterable):
            for index, i in enumerate(iterable[:-1]):
                if iterable[index+1] != i:
                    return False
            return True


        def __str__(self):
            out = ""
            brd = self.brd[::-1]
            for i in range(self.size):
                row = brd[self.size*i:self.size*(i+1)][::-1]
                for j, p in enumerate(row):
                    out += (p if p != TTT.Board.BLANK else "_" if i != self.size-1 else " ") + ("|" if j != self.size-1 else "")
                out += '\n' if i != self.size-1 else ""
            return out

        def __repr__(self):
            return self.__str__()


def foo(board, n, piece):
    """
    Return number of rows, columns, or diagonals with
    n number of pieces
    :param board: type TTT.Board
    :param n: number of exact piecs required on the row, col or diag
    :param piece: piece to count for on the row, col or diag
    """
    all_row_cols = get_row_cols(board)
    all_diags = get_diagonals(board)
    total = 0
    for i in all_row_cols:
        total += i.count(piece) == n

    for diag in all_diags:
        total += diag.count(piece) == n

    return total

def get_row_cols(board):
    """
    given a board, return all rows and columns in a nested list
    """
    row_and_cols = []
    size = board.size
    brd = board.brd
    for i in range(size):
        row = brd[i*size:(i+1)*size]
        row_and_cols.append(row)
        col = [brd[i+(size*j)] for j in range(size)]
        row_and_cols.append(col)
    return row_and_cols


def get_diagonals(board):
    """
    given a board, return both diagonals in a nested list with
    the first element as diagional \ and second element as diagonal /
    """
    size = board.size
    brd = board.brd
    diag1 = [brd[i*(size-1)+(size-1)] for i in range(size)]
    diag2 = [brd[i*(size+1)] for i in range(size)]
    return [diag1, diag2]
