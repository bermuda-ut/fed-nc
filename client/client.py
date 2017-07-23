from noughtsandcrosses import board, piece, InvalidMoveException
from human import humanplayer
from fed2  import federatedplayer

def main():
	b = board()
	ps = {
		piece.X: federatedplayer(piece.X),
		piece.O: humanplayer(piece.O)
	}
	print("player X: federatedplayer")
	print("player O: humanplayer")

	move = None
	error = None
	p = piece.X

	print("begin!")
	while b.playing():
		print("\n{}".format(b))

		print("{}s turn".format(p))
		ps[p].update(move)
		move = ps[p].move()
		
		try:
			b.move(move, p)
		except InvalidMoveException as e:
			error = e
			break

		p = piece.other(p)

	if error:
		print(error)
	else:
		print(b)
		ps[p].update(move)
		print("game over! winner: {}".format(b.winner()))

if __name__ == '__main__':
	main()
