class piece:
	X, O = 'X', 'O'
	blank = ' '
	@staticmethod
	def other(p):
		return piece.O if p == piece.X else piece.X

class board:
	def __init__(self):
		self.grid = [[piece.blank for j in range(3)] for i in range(3)]
	def __str__(self):
		rows = [" | ".join(row) for row in self.grid[::-1]]
		board = " " + " \n---+---+---\n ".join(rows) + "\n"
		return board
	def move(self, move, p):
		if move < 1 or move > 9:
			raise Exception("invalid move: {}".format(move))
		
		# find that part of the grid
		m = move - 1
		i, j = m // 3, m % 3
		
		# make sure it's legal
		if self.grid[i][j] != piece.blank:
			raise InvalidMoveException("invalid move: {} (space already occupied)".format(move))

		# make the actual move
		self.grid[i][j] = p
		
	def playing(self):
		return True

class InvalidMoveException(Exception):
	"""Raised due to an invalid move"""