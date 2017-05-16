import numpy as np


class Player:
	def __init__(self, piece):
		self.piece = piece
		self.phrase = "\nIt's the {0} player's turn.".format(self.piece)
		self.piece_value = 1 if self.piece == 'X' else 10
		self.winning_value = 3 if self.piece == 'X' else 30


class Board:
	def __init__(self, board_size=(3,3)):
		self._board_size = board_size
		self._board_array = np.zeros(self._board_size)
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
	def printPiece(self, value):
		if value == 0.0:
			return ' '
		elif value == 1:
			return 'X'
		else:
			return 'O'
	def printBoard(self):
		print('\n   1 | 2 | 3')
		count = 0
		for rows in self._board_array:
			count += 1
			print('{}: {} | {} | {}'.format(count, self.printPiece(rows[0]), self.printPiece(rows[1]), self.printPiece(rows[2])))
	def switchCurrentPlayer(self):
		self._current_player_num = (self._current_player_num + 1) % 2
		self.current_player = self.players[self._current_player_num]
	def checkWinningBoard(self):
		for piece in self.players:
			if piece.winning_value in np.sum(board(), axis=1):
				print("%s Wins!\n" % piece.piece)
				self.printBoard()
				return True
			elif piece.winning_value in np.sum(board(), axis=0):
				print("%s Wins!\n" % piece.piece)
				self.printBoard()
				return True
			elif np.sum(np.diag(np.flipud(board()))) == piece.winning_value:
				print("%s Wins!\n" % piece.piece)
				self.printBoard()
				return True
			elif np.sum(np.diag(board())) == piece.winning_value:
				print("%s Wins!\n" % piece.piece)
				self.printBoard()
				return True
			else:
				return False
	def spotIsTaken(self, x, y):
		if self._board_array[x-1][y-1] == 0.0:
			return False
		else:
			return True
	def checkDrawGame(self):
		empty_cells_list = [element for row in self._board_array for element in row]
		if empty_cells_list.count(0.0) == 0:
			print('\n---------------')
			print('Game is a draw!')
			print('---------------\n')
			return True
		else:
			return False


board = Board()


def startGame():
	print('Welcome to tictactoe!')
	while True:
		board.printBoard()
		print(board.current_player.phrase)
		row_coords = input('Enter row coordinates to place an %s > ' % board.current_player.piece)
		col_coords = input('Enter column coordinates to place an %s > ' % board.current_player.piece)
		row_coords, col_coords = int(row_coords), int(col_coords)
		if not board.spotIsTaken(row_coords, col_coords):
			board[row_coords-1][col_coords-1] = board.current_player.piece_value
			board._total_moves += 1
			if board.checkWinningBoard():
				break
			board.switchCurrentPlayer()
			if board.checkDrawGame():
				break
		else:
			print('\n-------------------------------------')
			print("Space is occupied.  Please try again.")
			print('-------------------------------------\n')


if __name__ == '__main__':
	startGame()


