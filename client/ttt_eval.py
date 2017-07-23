from noughtsandcrosses import piece
from ttt import get_row_cols, get_diagonals, TTT

class TutorialEvaluator:
    def __init__(self, p, weights):
        self.piece = p.lower()
        self.other = piece.other(p)

        self.weights = weights

    def evaluate(self, board):

        # get features

        # multiply by weights

        # return evaluation

        # given a board, count the number of rows,cols and diagonals
        # with exactly one x

        # the given eval in AI is:
        # eval = 3 * foo(board, 2, 'x') + foo(board, 1, 'x') - (3 * foo(board, 2, 'o') + foo(board, 1, 'o'))
        # and evaluate(self, board) should return +1, -1, 0 during
        # terminal states and draws (i don't think the eval = 3 * foo ..  actually gets these values)

        if board.draw():
            return 0
        winner = board.get_winner()

        if not winner:
            return 3 * self.foo(board, 2, TTT.Board.X) + \
                self.foo(board, 1, TTT.Board.X) - \
                (3 * self.foo(board, 2, TTT.Board.O) + \
                self.foo(board, 1, TTT.Board.O))
        return 1 if winner == self.piece else -1


    def max(self):
        """upper bound on evaluation"""
        pass
    def min(self):
        """lower bound on evaluation"""
        pass

    def foo(self, board, n, piece):
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

