#making a board right now
#this is a list that will store all the positions
grid = [["x"," "," "],
		["x","x"," "],
		[" "," ","o"]]

nums = ["1","2","3"];
currentPlayer = "x"
computer = False
empty = True

def greet():
	print("Hello")
	print("Let's play Tic-Toc-Toe")
	print("here's the board")
	displayBoard()

def displayBoard():
	print(grid[0])
	print(grid[1])
	print(grid[2])

def whoPlays():
	#to alternate players
	if computer == False:
		currentPlayer == "x"
		youMove()
	else:
		currentPlayer == "o"
		computerMove()
 
def youMove():
	#ask for user input to pick the row and column in the 2-d array
	while True:
		moveRow = input("Which row do you like to place your move(1-3)")
		if moveRow in nums:
			print(moveRow)
			break
	while True:
		moveCol = input("Which column do you like to place your move(1-3)")
		if moveCol in nums:
			break
	placeCheck(int(moveRow)-1,int(moveCol)-1)
	#user input's round is over, switch to computer
	computer = True

def computerMove():
	#check the first round
	for spot in grid:
		if grid[spot] == "o"



	computer = False

def placeCheck(x,y):	
	if grid[x][y] == " ":
		print("")
		print("you placed your move at row %d and column %d." % (x+1,y+1))
		grid[x][y] = "x"
		displayBoard()
		print("")
		checkWinner()
	else:
		print("you can't place it here.")
		youMove()

#check if the grid is full
for spot in grid:
	if spot == "":
		empty = true

def checkWinner():
	#winning combination is the list below 
	winning = ["x","x","x"]
	if grid[0] == winning  or \
		grid[1] == winning or \
		grid[2] == winning or \
		[grid[0][0],grid[1][0],grid[2][0]] == winning or \
		[grid[0][1],grid[1][1],grid[2][1]] == winning or \
		[grid[0][2],grid[1][2],grid[2][2]] == winning or \
		[grid[0][0],grid[1][1],grid[2][2]] == winning or \
		[grid[0][2],grid[1][1],grid[2][0]] == winning:
		print("you win!")
	elif empty == True:
		whoPlays()
	else:
		print("you lose")
			


greet()
checkWinner()

