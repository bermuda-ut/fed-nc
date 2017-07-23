"""
connects to server, gets an updated model, then plans a normal human-controlled
game anyway
"""

from noughtsandcrosses import piece
import flip
from alpha_beta import AlphaBeta
from ttt import TTT

class federatedplayer:
	def __init__(self, p):
		self.board = TTT(3, p)
		self.agent = AlphaBeta(4)
		
		# get the model from the server
		self.server = flip.flip()
		self.server.connect()
		self.server.send_check()
		model = self.server.recv_model()
		self.server.disconnect()

		self.weights = model.ws
		print(self.weights)

	def update(self, move):
		self._apply(move)
	def move(self):
		move = self._move()
		self._apply(move)
		return move
	
	def _apply(self, move):
		self.board.update(move)

	def _move(self):
		return self.agent.next_move(self.board)
