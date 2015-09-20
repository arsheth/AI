import pegSolitaireUtils
import config
import sys
import copy

def ItrDeepSearch(pegSolitaireObject):
	#################################################
	# Must use functions:
	# getNextState(self,oldPos, direction)
	# 
	# we are using this function to count,
	# number of nodes expanded, If you'll not
	# use this grading will automatically turned to 0
	#################################################
	#
	# using other utility functions from pegSolitaireUtility.py
	# is not necessary but they can reduce your work if you 
	# use them.
	# In this function you'll start from initial gameState
	# and will keep searching and expanding tree until you 
	# reach goal using Iterative Deepning Search.
	# you must save the trace of the execution in pegSolitaireObject.trace
	# SEE example in the PDF to see what to save
	#
	#################################################
	depth = 1
	copySolitaireObject = copy.deepcopy(pegSolitaireObject)
	gameState = pegSolitaireObject.gameState
	
	#getting possible start states for the initial configuration of game
	startStates = getStartStates(gameState)
	
	for startPos in startStates:
		#pegSolitaireObject = copySolitaireObject
		for depth in range(10):
			flag = playGame(pegSolitaireObject, startPos, gameState, depth)
			if flag == 1:
				return True
			if flag == -1:
				print "return -1...."	
				break;
			print "return 0..."
		pegSolitaireObject = copySolitaireObject
			
	
	return True


def getStartStates(gameState):
	
	startStates = []
	for i in range(7):
		for j in range(7):
			if gameState[i][j] == 1:
				startStates.append([i,j])

	return startStates



def playGame(pegSolitaireObject, startPos, prevGameState, depth):
	print "depth ", depth		
	result_flag = -1;

	if check_goal_state(pegSolitaireObject.gameState) :
		return 1
	elif depth == 0:
	
		print "backtracking to old state ", prevGameState
		print "current state ", pegSolitaireObject.gameState
		pegSolitaireObject.gameState = prevGameState
		
		return 0
	else:
		for direction in config.DIRECTION:
			print "direction ", config.DIRECTION[direction][0], config.DIRECTION[direction][1]
			
			
			prevGameState = copy.deepcopy(pegSolitaireObject.gameState)
			newGameState = pegSolitaireObject.getNextState(startPos, config.DIRECTION[direction])
			print "updated state ", newGameState
			if newGameState != None:
				print "next state ", startPos[0], startPos[1]
				states = getStartStates(newGameState)
				#trace = {startPos}

				for s in states:
					result_flag = playGame(pegSolitaireObject, s, prevGameState, depth-1)
					if result_flag == 1:
						return 1
		

		#states = getStartStates(gameState)
	'''	
		if len(states) == 0 : return -1
		

		for s in states:
			#update trace with startPos
			#call util nextState that updates game state
			# newGameState
			for direction in config.DIRECTION:
				newGameState = pegSolitaireUtils.getNextState(s, direction) 			
			
			result_flag = playGame(s, newGameState, depth-1)
			if result_flag:
				return 1
	'''

	return result_flag


def check_goal_state(gameState):
	
	for i in range(7):
		for j in range(7):
			if gameState[i][j] == 1:
				if i != 3 and j != 3:
					return False
			
	if gameState[3][3] == 0:
		return False
	
	return True


def aStarOne(pegSolitaireObject):
	#################################################
        # Must use functions:
        # getNextState(self,oldPos, direction)
        # 
        # we are using this function to count,
        # number of nodes expanded, If you'll not
        # use this grading will automatically turned to 0
        #################################################
        #
        # using other utility functions from pegSolitaireUtility.py
        # is not necessary but they can reduce your work if you 
        # use them.
        # In this function you'll start from initial gameState
        # and will keep searching and expanding tree until you 
	# reach goal using A-Star searching with first Heuristic
	# you used.
        # you must save the trace of the execution in pegSolitaireObject.trace
        # SEE example in the PDF to see what to return
        #
        #################################################
	return True	

def aStarTwo(pegSolitaireObject):
	#################################################
        # Must use functions:
        # getNextState(self,oldPos, direction)
        # 
        # we are using this function to count,
        # number of nodes expanded, If you'll not
        # use this grading will automatically turned to 0
        #################################################
        #
        # using other utility functions from pegSolitaireUtility.py
        # is not necessary but they can reduce your work if you 
        # use them.
        # In this function you'll start from initial gameState
        # and will keep searching and expanding tree until you 
        # reach goal using A-Star searching with second Heuristic
        # you used.
        # you must save the trace of the execution in pegSolitaireObject.trace
        # SEE example in the PDF to see what to return
        #
        #################################################
	return True
