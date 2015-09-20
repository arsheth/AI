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
	
	stackGS = []
	
	#for startPos in startStates:
		#pegSolitaireObject = copySolitaireObject
	for depth in range(10):
			#flag = playGame(pegSolitaireObject, startPos, gameState, depth)
		flag = playGameNew(pegSolitaireObject, depth, stackGS)
		if flag == 1:
			return True
		if flag == 0:
			del stackGS[:]
						
	
	return True


def getStartStates(gameState):
	
	startStates = []
	for i in range(7):
		for j in range(7):
			if gameState[i][j] == 1:
				startStates.append([i,j])

	return startStates


def playGameNew(pegSolitaireObject, depth, stackGS):
	if check_goal_state(pegSolitaireObject.gameState) :
		print "getting goal state...."
		return 1
	elif depth == 0:	
		return 0
	
	result = 0
	for i in range(7):
		for j in range(7):
			if pegSolitaireObject.gameState[i][j] == 1:
				for direction in config.DIRECTION:
					print "checking valid move for depth",i, j, depth
					flag = pegSolitaireObject.is_validMove([i, j], config.DIRECTION[direction])	
					if flag == True:
						pegSolitaireCopy = copy.deepcopy(pegSolitaireObject)
						print "initial state ", pegSolitaireCopy.gameState
						pegSolitaireCopy.getNextState([i, j], config.DIRECTION[direction])
						print "updated state ", pegSolitaireCopy.gameState
						#stackGSi.append(pegSolitaireCopy)
						result = playGameNew(pegSolitaireCopy, depth-1, stackGS)
						pegSolitaireObject.nodesExpanded = pegSolitaireCopy.nodesExpanded 
										
		
						if result == 1:	
							pegSolitaireObject.trace = pegSolitaireCopy.trace						
							return 1
						



	return result

'''
def playGame(pegSolitaireObject, depth):
	print "depth ", depth		
	result_flag = -1;

	if check_goal_state(pegSolitaireObject.gameState) :
		return 1
	elif pegSolitaireObject.gameState == None:
		return -1
	elif depth == 0:	
		return 0
	else:
		
		newGameState = pegSolitaireObject.getNextState(startPos, direction)


		playGame(pegSolitaireObject, startPos, config.DIRECTION['N'], depth)
		playGame(pegSolitaireObject, startPos, config.DIRECTION['S'], depth)
		playGame(pegSolitaireObject, startPos, config.DIRECTION['E'], depth)
		playGame(pegSolitaireObject, startPos, config.DIRECTION['W'], depth)
		

		if newGameState != None:
			print "next state ", startPos[0], startPos[1]

		states = getStartStates(newGameState)
				#trace = {startPos}
		for s in states:
			playGame(pegSolitaireObject, s, config.DIRECTION['N'], depth-1)
			playGame(pegSolitaireObject, s, config.DIRECTION['S'], depth-1)
			playGame(pegSolitaireObject, s, config.DIRECTION['E'], depth-1)
			playGame(pegSolitaireObject, s, config.DIRECTION['W'], depth-1)


			if result_flag == 1:
				return 1
		

		#states = getStartStates(gameState)

	return result_flag
'''

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
