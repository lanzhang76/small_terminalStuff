game = [["1","2","3"],
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]]

pl = True #pl true = you play versus false => 
noWinner = True

def board():
	for row in enumerate(game):
		print(row)

#check winners
def winner(check):
	if check.count(check[0]) == len(check) and check[0] != " ":
		if check[0] == "x":
			print("x win!")
			noWinner == False
		else:
			print("0 wins!")
			noWinner == False
	return noWinner

##horizontal win
def horizontal():
	for row in game[1:]:
		status = winner(row)
	return status

##vertical win
def vertical():
	game1 = game[1:]
	for col in range(3):
		check = []
		for row in range(3):
			check.append(game1[row][col])
		winner(check)

##diagonal win 
def diagonal():
	game1 = game[1:]
	checkj = []
	checki = []
	for j in range(len(game1)):
		checkj.append(game1[j][j])
	winner(checkj)
	for i in enumerate(reversed(range(len(game1)))):
		checki.append(game1[i[0]][i[1]])
	winner(checki)


#place move
def placeMove(gameboard, player):		
	try:
		status = diagonal()
		horizontal()
		vertical()
		global pl
		move = input("which row and column you want to place?")
		row = int(move[0])
		col = int(move[1])-1
		if player == True and gameboard[row][col] == " ":
			gameboard[row][col] = 'x'
			#board()
			pl = False
		elif player == False and gameboard[row][col] == " ":
			gameboard[row][col] = '0'
			#board()
			pl = True
		#print(pl)
	except IndexError as e:
		print("row and col plz.",e)
		#there's error doing error handling
	return gameboard



#actual procedual:

while noWinner:
	print(noWinner)
	board()
	game = placeMove(game, pl)
	#break
else:
	exit()
	














