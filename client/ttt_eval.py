from noughtsandcrosses import piece

class TutorialEvaluator:
	def __init__(self, p, weights):
		self.piece = p
		self.other = piece.other(p)

		self.weights = weights

	def evaluate(self, board):
		pass

		# get features

		# multiply by weights

		# return evaluation


	def max(self):
		"""upper bound on evaluation"""
		pass
	def min(self):
		"""lower bound on evaluation"""
		pass