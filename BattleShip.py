from random import randint

board =[]
##Create board 

for x in range(0,5):
	board.append(["O"]*5)
	
def printBoard(board):
	for row in board:
		print " ".join(row)

printBoard(board)

def randomRow(board):
	return randint(0, len(board)-1)
def randomCol(board):
	return randint(0, len(board)-1)

shipR = randomRow(board)
shipC = randomCol(board)
print shipR
print shipC


for turn in range(4):
	print "Turn" , turn +1 
	guessRow = int(raw_input("Guess Row: "))
	guessCol = int(raw_input("Guess Col: "))
	
	if guessRow == shipR and guessCol == shipC:
		print "Congrats! You sank my battleship!"
		break
	else:
		if guessRow not in range(5) or guessCol not in range(5):
			print "Out of Range, Try again"
		
		elif board[guessRow][guessCol] == "X":
			print "You guess that one already"
		else:
			print "You Missed!"
			board[guessRow][guessCol] = "X"
			if turn == 3:
				print "GAME OVER"
		printBoard(board)