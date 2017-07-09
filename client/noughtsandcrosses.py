class piece:
	X, O = 'X', 'O'
	@staticmethod
	def other(p):
		return piece.O if p == piece.X else piece.X

class board:
	def __init__(self):
		self.grid = [[str(i+j) for j in range(3)] for i in range(1, 9, 3)]
	def __str__(self):
		rows = [" | ".join(row) for row in self.grid[::-1]]
		board = " " + " \n---+---+---\n ".join(rows) + "\n"
		return board
	def move(self, move, p):
		if len(move) != 1 or move not in "123456789":
			raise Exception("invalid move: {}".format(move))
		
		# find that part of the grid
		m = int(move) - 1
		i, j = m // 3, m % 3
		
		self.grid[i][j] = p
