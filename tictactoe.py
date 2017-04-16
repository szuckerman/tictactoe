
class Board:
	def __init__(self):
		self.board_array = [[" " for _ in range(3)] for _ in range(3)]
	def __call__(self):
		return self.board_array
	def printBoard(self):
			print('1 | 2 | 3')
			count = 0
		for rows in self.board_array:
			count += 1
			print('{}: {} | {} | {}'.format(count, rows[0], rows[1], rows[2]))



class Player:
	def __init__(self, piece):
		self.piece = piece
		self.phrase = "It's the {0} player's turn.  Please select coordinates to place an {0}.".format(self.piece)


player1 = Player('X')
player2 = Player('O')

board = Board()

num_moves = 0

print('Welcome to tictactoe!')
while num_moves < 9:
	print(player1.phrase)
	move = input()
	x, y = move.split(',')
	x, y = int(x), int(y)
	board.board_array[x-1][y-1] = player1.piece
	board.printBoard()
	num_moves += 1
	print(player2.phrase)
	move = input()
	x, y = move.split(',')
	x, y = int(x), int(y)
	board.board_array[x-1][y-1] = player2.piece
	board.printBoard()
	num_moves += 1

	
