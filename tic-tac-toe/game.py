# we need a board with 9 slots, two players alternate, eventually one needs to be pc
# player one is "x", player two/future computer is "o"
import random

winner = "F" # "F" is false, "T" is true, "P" is tie
playerOne = True 
# top: 0,0 0,1 0,2
# mid: 1,0 1,1 1,2
# bot: 2,0 2,1 2,2
board = [[" "," "," "],
		 [" "," "," "],
		 [" "," "," "]]

def playerAlt(playerOne):
	# alternate players
	if playerOne == True:
		playerOne = False
	else:
		playerOne = True
	return playerOne


def getInput():
	# get and parse user input
	try:
		slot = input("where do you want to place your move?(row-space-col)\n").split(" ")
		slot = [int(slot[0])-1,int(slot[1])-1]
	except:	
		slot = input('please format your input as "row col"\n').split(" ")
		slot = [int(slot[0])-1,int(slot[1])-1]
	return slot


def placeMove(slot, board, playerOne):
	# check empty, if so ask for input to place move again
	# check if the slot is empty
	# if it's empty, place move based on player 
	if board[slot[0]][slot[1]] != "x" and board[slot[0]][slot[1]] != "o":
		if playerOne == True:
			board[slot[0]][slot[1]] = "x"
		else:
			board[slot[0]][slot[1]] = "o"
		player = playerAlt(playerOne)	
	else:
		print("you can't place your move there.\n")
		player = playerOne
	return player	


def checkWinner(board):
	# when called, checkWinner checks all ways one can win on the board
	winState = "F"
	# check any spot after winning condition is met
	def checkSpot(slot,state):
		#print(state) # used to check which cond has bug
		if slot == "x":
			print("player x wins!")
		elif slot == "o":
			print("player o wins!")
		winner = "T"
		return winner

	# horizontal win
	hor = []
	for r in range(len(board)):
		for c in range(len(board)):
			hor.append(board[r][c])
		if hor.count(hor[0]) == len(hor) and hor[0] != " ":
			winState = checkSpot(hor[0],"hor")
		hor = []

	# vertical win
	vert = []
	for r in range(len(board)):
		for c in range(len(board)):
			vert.append(board[c][r])	
		if vert.count(vert[0]) == len(vert) and vert[0] != " ":
			winState = checkSpot(vert[0],"vert")
		vert = [] # empties the list for every col

	# diagonal win
	diag = []
	diag2= []
	for i,b in enumerate((board)):
		diag.append(board[i][i])
		diag2.append(board[i][len(board)-1-i])
	if diag.count(diag[0]) == len(diag) and diag[0] != " ":
		winState = checkSpot(diag[0],"diag")
	if diag2.count(diag2[0]) == len(diag2) and diag2[0] != " ":	
		winState = checkSpot(diag2[0],"diag")

	# tie situation
	all = []
	for x in range(len(board)):
		for y in range(len(board)):
			all.append(board[x][y])
	if " " not in all and winState != "T":
		winState = "P"		

	return winState

	
def printBoard(board):
	print("")
	for i in range(len(board)):
		print(board[i])
	print("")


def generateInp():
	# pick a random spot
	row = random.randrange(0,3)
	col = random.randrange(0,3)
	return row,col

def checkUpdate(board):
	check = []
	for r in range(len(board)):
		for c in range(len(board)):
			check.append(board[r][c])
	empty = check.count(" ") # outputs an int
	return empty		



# the actual game runs here:
while(winner == "F"): 
	# check every round if there is a winner
	winner = checkWinner(board)
	if winner == "T":
		printBoard(board)
		print("One player has won. Game over!\n")
		break	
	elif winner == "P":
		print("Two players tied!\n")
		break
	
	# no winner, display board

	if playerOne == True:
		# human input 
		inp = getInput()
	else:	
		#computer input
		inp = generateInp()
	currentMove = checkUpdate(board)	
	playerOne = placeMove(inp,board,playerOne)
	nextMove = checkUpdate(board)

	if currentMove != nextMove:
		printBoard(board)










