from noughtsandcrosses import board, piece

def main():
	b = board()

	p = piece.X

	while True:
		# get move from user
		print(b)
		move = input("your move: ")

		# make move
		b.move(move, p)
		p = piece.other(p)
		

if __name__ == '__main__':
	main()