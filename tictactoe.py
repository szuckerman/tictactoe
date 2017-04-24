
class Player:
	def __init__(self, piece):
		self.piece = piece
		self.phrase = "\nIt's the {0} player's turn.  Please select coordinates to place an {0}.".format(self.piece)


class Board:
	def __init__(self):
		self._board_array = [[" " for _ in range(3)] for _ in range(3)]
		self.players = [Player('X'), Player('O')]
		self._current_player_num = 0
		self.current_player = self.players[self._current_player_num]
		self._total_moves = 0
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
	def switchCurrentPlayer(self):
		self._current_player_num = (self._current_player_num + 1) % 2
		self.current_player = self.players[self._current_player_num]
		#print('%s is the current player.' % self._current_player_num)


board = Board()


def checkWinningBoard():
	for piece in {'X', 'O'}:
		if board[0][0] == board[0][1] == board[0][2] == piece:
			print("%s Wins!\n" % piece)
			return True
		elif board[1][0] == board[1][1] == board[1][2] == piece:
			print("%s Wins!\n" % piece)
			return True
		elif board[2][0] == board[2][1] == board[2][2] == piece:
			print("%s Wins!\n" % piece)
			return True
		# Cols
		elif board[0][0] == board[1][0] == board[2][0] == piece:
			print("%s Wins!\n" % piece)
			return True
		elif board[0][1] == board[1][1] == board[2][1] == piece:
			print("%s Wins!\n" % piece)
			return True
		elif board[0][2] == board[1][2] == board[2][2] == piece:
			print("%s Wins!\n" % piece)
			return True
		# Diagonal
		elif board[0][0] == board[1][1] == board[2][2] == piece:
			print("%s Wins!\n" % piece)
			return True
		elif board[2][0] == board[1][1] == board[0][2] == piece:
			print("%s Wins!\n" % piece)
			return True
		else:
			return False


# def checkIfSpotTaken(x, y):
# 	if board[x-1, y-1] != ' ':


print('Welcome to tictactoe!')
while True:
	board.printBoard()
	print(board.current_player.phrase)
	move = input()
	x, y = move.split(',')
	x, y = int(x), int(y)
	board[x-1][y-1] = board.current_player.piece
	board._total_moves += 1
	if checkWinningBoard():
		break
	board.switchCurrentPlayer()

