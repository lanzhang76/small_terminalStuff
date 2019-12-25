# import random

# board = [["x"," "," "],
# 		 [" ","x"," "],
# 		 [" "," ","x"]]


# # def getRandSpot():
# # 	row = random.randrange(0,3)		 
# # 	col = random.randrange(0,3)	
# # 	return row,col	

# # r,c = getRandSpot()
# # while board[r][c] == "x" or board[r][c] == "o":
# # 	r,c = getRandSpot()
# # else:
# # 	board[r][c]="o"	

# # print(board)

# hor =[]
# vert = []
# dia = []
# dia2 = []

# for r in range(len(board)):
# 	for c in range(len(board)):
# 		hor.append(board[r][c])
# 	if hor.count("x") == 2:
# 		board[r][hor.index(" ")] = "o"
# 	hor = []
# print(board)