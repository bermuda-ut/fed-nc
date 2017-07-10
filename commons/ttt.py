from client.noughtsandcrosses import InvalidMoveException

class TTT(object):
    class Board(object):
        BLANK = " "
        def __init__(self, size):
            self.size = size
            self.brd = [TTT.Board.BLANK]*(size*size)

        def update(self, move, piece):
            """
            updates the internal board in-place
            """
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
            diag1 = [self.brd[i*(self.size-1)+(self.size-1)] for i in range(self.size)]
            if TTT.Board._all_same(diag1) and diag1[0] != TTT.Board.BLANK:
                return diag1[0]
            # / diagonal
            diag2 = [self.brd[i*(self.size+1)] for i in range(self.size)]
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

    def __init__(self, size, piece):
        self.state = TTT.Board(size)
        self.piece = piece

    def update(self, action):
        """
        apply action *in-place* on the board itself
        """
        self.state.update(action, self.piece)

    def apply_action(self, action):
        """
        returns the new board after action is applied on a copy of the current board,
        the current board is not changed
        """

        copy_ttt = self.clone()
        copy_ttt.state.update(action, self.piece)
        return copy_ttt

    def get_actions(self):
        return [(index + 1) for index, pos in enumerate(self.state.brd) if pos == TTT.Board.BLANK]

    def evaluate(self):
        return 1

    def is_terminal(self):
        return self.state.get_winner() != None


    def clone(self):
        """
        returns a deep copy of this TTT state
        """
        # create a new copy of TTT
        new_copy = TTT(self.state.size, self.piece)
        # override the empty board
        new_copy.state.brd = list(self.state.brd)
        return new_copy
