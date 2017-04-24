
class Board:
	def __init__(self):
		self._board_array = [[" " for _ in range(3)] for _ in range(3)]
	def __getitem__(self, i):
		return self._board_array[i]
	def __setitem__(self, i, val):
		self._board_array[i] = val
	def __call__(self):
		return self._board_array
	def printBoard(self):
		print('   1 | 2 | 3')
		count = 0
		for rows in self._board_array:
			count += 1
			print('{}: {} | {} | {}'.format(count, rows[0], rows[1], rows[2]))


class Player:
	def __init__(self, piece):
		self.piece = piece
		self.phrase = "\nIt's the {0} player's turn.  Please select coordinates to place an {0}.".format(self.piece)


player1 = Player('X')
player2 = Player('O')

board = Board()

num_moves = 0


def checkWinningBoard():
	for piece in {'X', 'O'}:
		global num_moves
		if board[0][0] == board[0][1] == board[0][2] == piece:
			board.printBoard()
			print("%s Wins!\n" % piece)
			return True
		elif board[1][0] == board[1][1] == board[1][2] == piece:
			board.printBoard()
			print("%s Wins!\n" % piece)
			return True
		elif board[2][0] == board[2][1] == board[2][2] == piece:
			board.printBoard()
			print("%s Wins!\n" % piece)
			return True
		# Cols
		elif board[0][0] == board[1][0] == board[2][0] == piece:
			board.printBoard()
			print("%s Wins!\n" % piece)
			return True
		elif board[0][1] == board[1][1] == board[2][1] == piece:
			board.printBoard()
			print("%s Wins!\n" % piece)
			return True
		elif board[0][2] == board[1][2] == board[2][2] == piece:
			board.printBoard()
			print("%s Wins!\n" % piece)
			return True
		# Diagonal
		elif board[0][0] == board[1][1] == board[2][2] == piece:
			board.printBoard()
			print("%s Wins!\n" % piece)
			return True
		elif board[2][0] == board[1][1] == board[0][2] == piece:
			board.printBoard()
			print("%s Wins!\n" % piece)
			return True
		else:
			return False


print('Welcome to tictactoe!')
while True:
	board.printBoard()
	print(player1.phrase)
	move = input()
	x, y = move.split(',')
	x, y = int(x), int(y)
	board[x-1][y-1] = player1.piece
	board.printBoard()
	if checkWinningBoard():
		break
	num_moves += 1
	print(player2.phrase)
	move = input()
	x, y = move.split(',')
	x, y = int(x), int(y)
	board[x-1][y-1] = player2.piece
	if checkWinningBoard():
		break
	num_moves += 1
