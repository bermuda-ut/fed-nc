"""
connects to server, gets an updated model, then plans a normal human-controlled
game anyway
"""

from noughtsandcrosses import piece

import flip

from ttt_eval import TutorialEvaluator
from ttt import TTT
from alpha_beta import AlphaBeta

class federatedplayer:
	def __init__(self, p):	
		# get the model from the server
		model = self._download_model()

		# create an evaluator with these weights, and an ai agent using it
		evaluator = TutorialEvaluator(p, model)
		self.board = TTT(3, p, evaluator)
		self.agent = AlphaBeta(4)

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
	
	def _download_model(self):
		server = flip.flip()
		server.connect()
		server.send_check()
		model = server.recv_model()
		server.disconnect()
		return model
