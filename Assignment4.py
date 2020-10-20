#Author: Ethan Brydon
#Student Number: 101157918
#Date: 14/11/2019
#Purpose: This program implements a bunch of different functions that revolve hockey fantasy stats

import os.path
from os import path

#this funcion takes a file as a parameter and converts that file into a 2D list of playerStats 
def readStats(filename):
	
	stats = []
	
	#checks that the file exists
	#if it doesnt, a error message is printed and an empty list is returned  
	if path.exists(filename) != True:
		
		print(f"The file: {filename}. Does not exist.")
		return []
	
	#opens file and converts it to a string
	f = open(filename,'r')
	text = f.read()
	
	#initializing variables
	firstline = True
	start = 0
	end = 0
	
	#loops through the string and appends each player and their stats to a list, this creates the 2D list
	for i in range(0,906) :
		
		#skips first line of string
		if firstline == True:
			start = text.find('\n') + 1 
			firstline = False
		
		#initializing 2D array
		player = []
		
		#loops through the string and appends each stat to a list, this creates the 1D list for each player
		for j in range(0,11) :
		
			#gets each stat by slicing at commas and the last stat is sliced from the last comma to '\n'
			if j < 3:
				end = text.find(',',start)
				player.append(text[start:end])
				start = end + 1
				
			elif j == 10:
				end = text.find('\n',start)
				player.append(int(text[start:end]))
				start = end + 1
			
			else:
				end = text.find(',',start)
				player.append(int(text[start:end]))
				start = end + 1
		
		#adds the list of player stats to the list of stats
		stats.append(player)
	
	return stats

#This function takes a 2D list of stats and a player name as parameters and finds the list of that players stats  	
def statsForPlayer(statsList, playerName) :
	
	#loops through the list of stats to find the player  
	for i in range(0,len(statsList)) :
		
		#returns the list of the players stats when found 
		if statsList[i][0] == playerName:
			return statsList[i]
	
	#if the player isnt found then a empty string is returned
	return []	

#This function takes a 2D list of stats and a position as parameters and makes a list of only the players at the given position			
def filterByPos(statsList, pos) :
	
	#initializing 2D array
	positionList = []
	
	#loops through the stats list and appends the list of stats for each player that plays the given position
	for i in range(0,len(statsList)) :
		
		if statsList[i][2] == pos:
			positionList.append(statsList[i])
	
	return positionList

#This function takes a 2D list of stats and sorts it by points(pts) in descending order 
def sortByPoints(statsList)  :
	
	#initializes variables 
	sortedStats = []
	statsList = statsList[:]
	
	#loops through the list until the statsList is empty and appends the players lists with the highest points
	while len(statsList) > 0 :
		
		largest = -1
		largestIndex = 0
		
		for i in range(0, len(statsList)) :
		
			if statsList[i][6] > largest:
				largestIndex = i
				largest = statsList[i][6]
				
		sortedStats.append(statsList[largestIndex])
		statsList.pop(largestIndex)
		
	return sortedStats

#This function takes a 2D list of stats and a file name as parameters and fills the file with the names of the players with the most points at each position (2 defencemen) 
def buildBestTeam(statsList, filename) :
	
	#checks that the file exists
	#if it doesnt, a error message is printed and the function exits
	if path.exists(filename) != True:
		
		print(f"Error writing to this file {filename}.")
		return 
	
	#sorts the stats list by points
	sortedStatsList = sortByPoints(statsList)
	
	#creates lists sorted by position
	sortedCentre = filterByPos(sortedStatsList, 'C')
	sortedLeftWing = filterByPos(sortedStatsList, 'LW')
	sortedRightWing = filterByPos(sortedStatsList, 'RW')
	sortedDefence = filterByPos(sortedStatsList, 'D')
		
	#all these if and else statements get the names of the players with the most points at each position	
	if sortedCentre != []:
		centre = sortedCentre[0][0]
		
	else:
		centre = ""
	
	if sortedLeftWing != []:	
		leftWing = sortedLeftWing[0][0]
			
	else:
		leftWing = ""
	
	if sortedRightWing != []:
		rightWing = sortedRightWing[0][0]
				
	else:
		rightWing = ""
	
	if sortedDefence != []:
		defence1 = sortedDefence[0][0]
				
	else:
		defence1 = ""
	
	if len(sortedDefence) > 2:
		defence2 = sortedDefence[1][0]
					
	else:
		defence2 = ""
	
	try:
		#writes names of players into file 
		f = open(filename,'w')
		f.write(centre + "\n" + leftWing + "\n" + rightWing + "\n" + defence1 + "\n" + defence2)
		f.close()
		
	except:
		#checks that it can write to the file
		#if it doesnt, a error message is printed and the function exits
		print(f"Error writing to this file {filename}.")
		return 

#This function takes a 2D list of stats and a team file name as parameters and displays the stats for the players on the team	
def displayTeamStats(statsList, TeamFilename) :
	
	#checks that the file exists
	#if it doesnt, the function exits
	if path.exists(TeamFilename) != True:
		
		return
	
	#initializes variable
	start = 0
	
	#opens file and converts it to a array of strings of each line 
	f = open(TeamFilename,'r')
	lines = f.readlines()
	f.close()
	
	#prints the first 2 rows of the stats display table 
	print("Player Name"+" "*12+"\tTeam\t"+"Pos\t"+"Games\t"+"G\t"+"A\t"+"Pts\t"+"PIM\t"+"SOG\t"+"Hits\t"+"BS")
	print("="*104)
	
	#this loop prints the stats for each player 
	for i in range(0,len(lines)):
		
		player = lines[i]
		
		if i < len(lines) - 1: 
			player = player[0:len(player) - 1]
		
		playerStats = statsForPlayer(statsList,player)
		print(f"{playerStats[0]}"+" "*(23-len(playerStats[0]))+f"\t{playerStats[1]}\t{playerStats[2]}\t{playerStats[3]}\t{playerStats[4]}\t{playerStats[5]}\t{playerStats[6]}\t{playerStats[7]}\t{playerStats[8]}\t{playerStats[9]}\t{playerStats[10]}\t")

#This function takes a 2D list of stats and a team file name as parameters and calculates the total points for that team		
def pointsPerTeam(statsList, TeamFilename) :
	
	#checks that the file exists
	#if it doesnt, the function returns zero
	if path.exists(TeamFilename) != True:
		
		return 0
	
	#initializes variables
	pointsTotal = 0
	start = 0
	
	#opens file and converts it to a array of strings of each line 
	f = open(TeamFilename,'r')
	lines = f.readlines()
	f.close()
	
	#loops through, finds the stats for each player and adds their points to the points total
	for i in range(0,len(lines)):
		
		player = lines[i]
		
		if i < len(lines) - 1: 
			player = player[0:len(player) - 1]
			 
		playerStats = statsForPlayer(statsList, player)
		
		if playerStats == []:
			pointsTotal += 0
			
		else:
			pointsTotal += playerStats[6]
			
	return pointsTotal

#This function tests that all of the functions that were previously made operate correctly 	
#if they do it return True, if they do not it returns False  
def testing(excelStatsFile, fileThatDoesNotExist, bestTeamFile, sampleTeamFile) :
	
	test1 = readStats(excelStatsFile)
	
	test2 = readStats(fileThatDoesNotExist)
	
	test3 = statsForPlayer(test1, "Sidney Crosby")
	
	test4 = filterByPos(test1, 'D')
	
	test5 = sortByPoints(test1)
	
	buildBestTeam(test1, bestTeamFile)
	
	if path.exists(bestTeamFile) != True:
		
		#checks that it can read the file
		#if it doesnt, a error message is printed and the function exits
		print(f"Error reading this file {bestTeamFile}.")
		return False
	
	
	#reads in the filea as a list of strings for each line
	f = open(bestTeamFile,'r')
	lines = f.readlines()
	f.close()
	
	test6 = pointsPerTeam(test1, sampleTeamFile)
	
	if len(test1) != 906:
		return False
		
	if test2 != []:
		return False
		
	if test3[0] !=  "Sidney Crosby" and test3[1] != PIT:
		return False
	
	for i in range (0, len(test4)) :
		
		if test4[i][2] != 'D':
			return False 
			
	if test5[905][6] > test5[0][6]:
		return False 
	
	if path.exists(bestTeamFile) != True:
		return False 
		
	if len(lines) != 5:
		return False 
		
	if test6 != 311:
		return False 
		
	return True
		
def main() :	
	
	#gathers user input to use as parmeters for the testing function to test the code
	print("Enter the folowing strings to test the code.")
	excelStatsFile  = str(input("Enter the excel stats file name:\n>"))
	noFile = str(input("Enter a non-existent file name name:\n>"))
	bestTeamFile = str(input("Enter the best team file name name:\n>"))
	sampleTeamFile = str(input("Enter the sample team file name name:\n>"))
	
	#prints whether the tests were successful of not   
	print(testing(excelStatsFile, noFile, bestTeamFile, sampleTeamFile))

main()