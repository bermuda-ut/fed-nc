from noughtsandcrosses import piece

class humanplayer:
	def __init__(self, p):
		self.board = [[piece.blank for j in range(3)] for i in range(3)]
		self.piece = p
	def update(self, move):
		self._apply(move, piece.other(self.piece))
	def move(self):
		move = self._move()
		self._apply(move, self.piece)
		return move
	
	def _apply(self, move, p):
		if move:
			m = move - 1
			i, j = m // 3, m % 3
			self.board[i][j] = p

	def _move(self):
		print("")
		print("this is the board:")
		board = [[str(3*i+j+1) if self.board[i][j] == piece.blank else self.board[i][j] for j in range(3)] for i in range(3)]
		rows = [" | ".join(row) for row in board[::-1]]
		print(" " + " \n---+---+---\n ".join(rows))

		move = int(input("select your move: "))
		print("")
		return move
