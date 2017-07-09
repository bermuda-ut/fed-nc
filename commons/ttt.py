class TTT(object):
    class Board(object):
        BLANK = " "
        def __init__(self, size):
            self.size = size
            self.brd = [Board.BLANK]*(size*size)

        def update(self, move, piece):
            if self.brd[move-1] != Board.BLANK:
                raise Exception("Placing a piece on occupied position {} ".format(move) + \
                     "on board but piece {} already occupied position\n".format(self.brd[move-1]) + self.__str__())
            self.brd[move-1] = piece

        def __str__(self):
            out = ""
            brd = self.brd[::-1]
            for i in range(self.size):
                row = brd[self.size*i:self.size*(i+1)][::-1]
                for j, p in enumerate(row):
                    out += (p if p != Board.BLANK else "_" if i != self.size-1 else " ") + ("|" if j != self.size-1 else "")
                out += '\n' if i != self.size-1 else ""
            return out

        def __repr__(self):
            return self.__str__()

    def __init__(self, size, piece):
        self.state = Board(size)
        self.piece = piece

    def apply_action(self, action):
        self.state.brd.update(action, self.piece)

    def get_actions(self):
        return [pos for pos in self.state.brd if pos == Board.BLANK]

    def evaluate(self):
        return 1

    def is_terminal(self):
        return False
