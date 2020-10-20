#Author: Ethan Brydon
#Student Number: 101157918
#Date: 3/12/2019
#Purpose: This program is a ascii game that takes a row and column and a symbol as user input
# the progarm then uses these inputs to fill all the adjacent matching symbol to the symbol at 
# the row and column that were given. The game keeps asking the user for those 3 inputs until 
# the board is filled up with only one symbol. When this happens the level is complete. The 
# game is played for 5 levels and at the end the users total moves needed to complete all the 
# levels is outputted and the user is prompted to play again or not play again. If they wish 
# to play again then the game resets and they start at level 1. 

#This function takes a level number as parameter and takes the corresponding file and converts it
# into a 2D list that will represent the board for that level
def readLevel(lvl):
	
	#creats string of filename
	file = r'levels\ascii_fill_level'+str(lvl)+'.txt'
	
	#opens file if there is an error in doing so then a simple error message is printed and 
	# the function exits
	try:
		f = open(file, 'r')
		lines = f.readlines()
		f.close()
		
	except:
		print("There was a error with reading the file")
		return
	
	#initializes variable
	board = []
	
	#creats 2D list of board
	for j in range(len(lines)):
		list = []
		for i in range(len(lines[0])-1):
			list.append(lines[j][i])
		board.append(list)
		
	return board

#This function takes a 2D list represnting the board as a parameter and neatly
# displays the board for the user to see	
def displayBoard(list):
	
	#initializes variables
	digit = 0
	row1and2 = ["   ", "   "]
	
	#creates string of the first 2 columns of the display 
	for i in range(len(list[0])):
		if digit != 10:
			row1and2[0] += str(digit)
			row1and2[1] += "-"
			digit += 1
		else:
			digit = 0
			row1and2[0] += str(digit)
			row1and2[1] += "-"
			digit += 1
	
	#initializes list that will be used to display 2nd part of board 
	PartOfBoard = []
	
	#creates list for 2nd part of board
	for i in range(len(list)):
		row = ""
		if i < 10: 
			row += "0"+str(i)+"|"
		else:
			row += ""+str(i)+"|"
			
		for j in range(len(list[0])):
			row += list[i][j]
			
		PartOfBoard.append(row)
	
	#displays both 1st and 2nd parts of board, therefore displaying the whole thing
	print(row1and2[0])
	print(row1and2[1])	
	for i in range(len(PartOfBoard)):
		print(PartOfBoard[i])

#This function takes to integers representing row and column as parameters aand then 
# requests that the user input what symbol they would like to put there to fill the 
# board with, the function then returns these 3 variables as a list  	
def getUserAction(row, col):

	#initializes list 
	act = [row, col]
	#asks for the symbol the user would like to put 
	InputSymbol = str(input("What symbol would you like to put at ("+str(row)+","+str(col)+"): "))
	
	#checks that user inputed symbol is valid 
	while True:
		if InputSymbol in "&%#@" and InputSymbol != '':
			act.append(InputSymbol)
			return act
		else:
			InputSymbol = str(input("Please enter a valid symbol: "))

#This function takes the board, the targeted symbol, the inputed symbol, the row and column all as parameters
# and uses them to recursively fill the board with the inputed symbol by only switching all
# the adjacent targeted symbols with the inputed symbol 	
def fill(board, target, InputSymbol, row, col):
	
	#checks if target is equal to symbol, if so function terminates 
	if target == InputSymbol:
		return
	
	#checks for adjacent target to the left of the current index (if there is one), changes the char at that index
	# to the inputed symbol if the symbol there is the target, after the change the function returns a 
	# a call on itself from the index to the left and  from the current index. (*this whole process is done in the 
	# folowing code below for every direction (left,up,right,down) 
	try:
		if col != 0:
			if board[row][col-1] == target:
				board[row][col-1] = InputSymbol
				return fill(board, target, InputSymbol, row, col-1) + fill(board, target, InputSymbol, row, col)
	except:
		pass
	try:
		if row != len(board):
			if board[row+1][col] == target:
				board[row+1][col] = InputSymbol
				return fill(board, target, InputSymbol, row+1, col) + fill(board, target, InputSymbol, row, col)
	except:
		pass
	try:
		if col != len(board[0]):
			if board[row][col+1] == target:
				board[row][col+1] = InputSymbol
				return fill(board, target, InputSymbol, row, col+1) + fill(board, target, InputSymbol, row, col)
	except:
		pass
	try:
		if row != 0:
			if board[row-1][col] == target:
				board[row-1][col] = InputSymbol
				return fill(board, target, InputSymbol, row-1, col) + fill(board, target, InputSymbol, row, col)
	except:
		pass
		
	#if there is no adjacents then weve hit a deadend, so we change the symbol at the current 
	# location and nothing is returned
	board[row][col] = InputSymbol
	return

#This function runs the whole game, which was explained in the Purpose section
def main():
	
	#initializes variables
	level = 0
	totalMoves = 0
		
	#this loop runs the 5 levels of the game	
	for i in range(5): 
	
		#initializes things needed before the start of the level
		level += 1
		print("\n*LEVEL "+str(level)+"*\n")
		moves = 0
		boardNotComplete = True
		gameBoard = readLevel(level)
		displayBoard(gameBoard)
		
		#this loop continues to get the user to give an action until the board is 
		# only consisting of one symbol
		while boardNotComplete == True:
			
			#lines 171-212 ensure that the user inputs a valid row and column for their action
			# it does not accept non-int input or rows and columns not within the range of the board 
			try:
				row = int(input("\nSelect a row [0,"+str(len(gameBoard)-1)+"]: "))
				if row > len(gameBoard)-1 or row < 0:
					while True:
						try:
							row = int(input("Please enter a valid row: "))
		
							if row > len(gameBoard)-1 or row < 0:
								continue
						except:
							continue					
						break
			except:	
				while True:
					try:
						row = int(input("Please enter a valid row: "))
						
						if row > len(gameBoard)-1 or row < 0:
							continue
					except:
						continue
					break
			try:
				col = int(input("\nSelect a column [0,"+str(len(gameBoard[0])-1)+"]: "))
				if col > len(gameBoard[0])-1 or col < 0:
					while True:
						try:
							col = int(input("Please enter a valid column: "))
							if col > len(gameBoard[0])-1 or col < 0:
								continue
						except:
							continue
						break
			except:	
				while True:
					try:
						col = int(input("Please enter a valid column: "))
						if col > len(gameBoard[0])-1 or col < 0:
							continue
					except:
						continue
					break
			
			#creates user action
			action = getUserAction(row, col)
			
			#uses row and column to obtain target symbol before running fill
			target = gameBoard[row][col]
			
			#fills the board
			fill(gameBoard, target, action[2], action[0], action[1])
			
			#displays the new board
			print("\n")
			displayBoard(gameBoard)
			
			#adjusts some variables
			moves += 1
			indexAllSame = True
			
			#checks if the board only conists of one symbol
			for i in range(len(gameBoard)):
				for j in range(len(gameBoard[0])):
					if gameBoard[i][j] != gameBoard[0][0]:
						indexAllSame = False 
						break
				if indexAllSame == False:
					break
			
			if indexAllSame == True:
				boardNotComplete = False
		
		#tells the user how many moves they used to complete that level	
		print("Level "+str(level)+" completed in "+str(moves)+" moves!")
		
		#increases total moves by how many moves the user used to complete the level
		totalMoves += moves
	
	#after all 5 levels are completed the user is given some output to read and told how many 
	# moves it took them
	print("\nYou win! Thanks for playing.")
	print("You completed all 5 levels in "+str(totalMoves)+" moves!")
	
	#the user is asked if they would like to play the game again
	again = str(input("\nWould you like to play again ('y'=yes & 'n'=no): "))
	
	#checks for valid user input 
	while True:
		if again == 'y':
			return main()
		elif again == 'n':
			print("\nOkay bye! Have a nice day!")
			return 
		else:
			again = str(input("\nPlease enter a valid input ('y'=yes & 'n'=no): "))
	
main()
