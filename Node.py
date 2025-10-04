
from copy import deepcopy
import math

class Node:
    def __init__(self, board, gn=0):
        self.state = board
        #the number of moves to get to this state
        self.gn = gn
        self.parent = None
     
    def getMoves(self):
        nextStates = []
        nextGn = self.gn + 1

        #find the place where the blank is in the puzzle
        indexErow, indexEcol = self.findblankLoc(self.state)

        #get the length of row and columns for the boundries
        rows = len(self.state)
        cols = len(self.state[0])

        #Now we have to check if the empty piece can move up, down, left, or right
        #up
        if indexErow > 0:
            #creates a copy of the current state
            nextState = deepcopy(self.state)
            rowUp = indexErow - 1

            #swap the two tiles
            temp = nextState[rowUp][indexEcol]
            nextState[rowUp][indexEcol] = nextState[indexErow][indexEcol]
            nextState[indexErow][indexEcol] = temp
            
            #store the node in the list
            node = Node(nextState, nextGn)
            node.parent = self
            nextStates.append(node)

        #down
        if indexErow < rows - 1:
            #creates a copy of the current state
            nextState = deepcopy(self.state)
            rowDown = indexErow + 1

            #swap the two tiles
            temp = nextState[rowDown][indexEcol]
            nextState[rowDown][indexEcol] = nextState[indexErow][indexEcol]
            nextState[indexErow][indexEcol] = temp

            #store the node in the list
            node = Node(nextState, nextGn)
            node.parent = self
            nextStates.append(node)

        #left
        if indexEcol > 0:
            #creates a copy of the current state
            nextState = deepcopy(self.state)
            left_col_index = indexEcol - 1
            
            #swap the two tiles
            temp = nextState[indexErow][left_col_index]
            nextState[indexErow][left_col_index] = nextState[indexErow][indexEcol]
            nextState[indexErow][indexEcol] = temp

            #store the node in the list
            node = Node(nextState, nextGn)
            node.parent = self
            nextStates.append(node)

        #right
        if indexEcol < cols - 1:
            #creates a copy of the current state
            nextState = deepcopy(self.state)
            right_col_index = indexEcol + 1

            #swap the two tiles
            temp = nextState[indexErow][right_col_index]
            nextState[indexErow][right_col_index] = nextState[indexErow][indexEcol]
            nextState[indexErow][indexEcol] = temp            
            
            #store the node in the list
            node = Node(nextState, nextGn)
            node.parent = self
            nextStates.append(node)

        return nextStates

    #find indexes of the blank tile; set to value 0. 
    def findblankLoc(self, puzzle):
        for r in range(len(puzzle)):
            for c in range(len(puzzle)): #successfully reaches position (0,2) when running on player input
                if puzzle[r][c] == 0: #goes out of range here somehow, despite the loop staying within the intended size (I checked)
                    return r, c
        return None
    
    
