from client.noughtsandcrosses import InvalidMoveException

class TTT(object):
    class Board(object):
        BLANK = " "
        def __init__(self, size):
            self.size = size
            self.brd = [TTT.Board.BLANK]*(size*size)

        def update(self, move, piece):
            if self.brd[move-1] != TTT.Board.BLANK:
                raise InvalidMoveException("Placing a piece on occupied position {} ".format(move) + \
                     "on board but piece {} already occupied position\n".format(self.brd[move-1]) + self.__str__())
            self.brd[move-1] = piece

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

    def apply_action(self, action):
        """
        apply action 'inplace' on the board itself
        """
        self.state.update(action, self.piece)

    def apply_action_copy(self, action):
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
        return False

    def clone(self):
        """
        returns a deep copy of this TTT state
        """
        # create a new copy of TTT
        new_copy = TTT(self.state.size, self.piece)
        # override the empty board
        new_copy.state.brd = list(self.state.brd)
        return new_copy
