
from queue import PriorityQueue
from Node import Node
import math

class Problem:
    def __init__(self, puzzle, size):
        self.initialState = puzzle
        self.size = size
        self.que = PriorityQueue()
        self.explored = set()
        self.nodesSearched = 0
        self.maxQ = 0
        self.solution = []

        #creat goal state
        goal = []
        num = 1
        for i in range(size):
            row = []
            for j in range(size):
                row.append(num)
                num +=1
            goal.append(row)
        
        goal[size -1][size-1] = 0
        self.goalState = goal
    

      #find the path of nodes that lead to the goal state
    def findSolutionPath(self, node):
        path = []
        #trace the path and make sure we can get to the starting puzzle
        while node.parent != None:
            path.append(node.state)
            node = node.parent
        path.reverse()
        self.solution = path
    
    #print the path of nodes that lead to the goal state   
    def PrintSolutionPath(self):
        #reverse the list so it prints out in correct order
        print('------------------------------------------')
        print("Solution path is:")
        for state in self.solution:
            self.printPuzzle(state)
            print('--------')

    
    def printPuzzle(self, state):
        for i in range(len(state)):
            print(state[i])

    #print the goal ending message for when they finish
    def printGoalMes(self):
        print("Goal!!!")
        print("To solve this problem the search algorithm expanded a total of " + str(self.nodesSearched) + " nodes.")
        print("The maximum number of nodes in the queue at any one time was: " + str(self.maxQ))
        print("The depth of the goal node is: " + str(len(self.solution)))


    #Performs the uniform cost search on puzzle
    def UniCostSearch(self):
        #create the first node and variables to keep track of stats
        current = Node(self.initialState)
        nodesNum = 1
        count = 1
        
        #user message of expanding
        print("Expanding state")
        self.printPuzzle(current.state)
        print() #amshu - not sure if additional empty line is needed or not
        #check if inital state is the goal state
        if current.state == self.goalState:
            self.nodesSearched = nodesNum
            self.printGoalMes()
            return
        #count is used as measure for priority Queue
        item = (current.gn, count, current)
        self.que.put(item)
        #turn the state into tuple to make the search easier and imutable and 2D list cannot go in set
        tupleState = tuple(map(tuple, current.state))
        self.explored.add(tupleState)

        #search the queue until there is nothing to search or goal is reached
        while not(self.que.empty()):
            #update the maximum in queue
            self.maxQ = max(self.maxQ, self.que.qsize())
            #deque and add to explored
            first = self.que.get()
            current = first[2]
            tupleState = tuple(map(tuple, current.state))
            self.explored.add(tupleState)
            #check if inital state is the goal state
            if current.state == self.goalState:
                self.nodesSearched = nodesNum
                self.findSolutionPath(current)
                self.printGoalMes()
                self.PrintSolutionPath()
                return
            print("The best state to expand with g(n) = " + str(current.gn) + " is ...")
            self.printPuzzle(current.state)
            print("Expanding this node...")
            print('--------')
            #all possible next moves from current node
            pMoves = current.getMoves()
            #check all the moves and add to queue if not explored
            for node in pMoves:
                count += 1
                tupleState = tuple(map(tuple, node.state))
                if tupleState not in self.explored:
                    node.parent = current
                    item = (node.gn, count, node)
                    self.que.put(item)
            #increase depth count
            nodesNum += 1
        return
            
        
    def AStarSearch(self, heuristic):
        #initialize variable 
        current = Node(self.initialState)
        nodeNum =1 
        count = 1
        maxQ = 0

        print("Expanding state")
        self.printPuzzle(current.state)
        print()

        #check if the initial state is already a goal state
        if current.state == self.goalState:
            self.nodesSearched = nodeNum
            self.printGoalMes()
            return

        #calculate f(n)=g(n)+h(n)
        hn= heuristic(current.state, self.goalState)
        fn = current.gn + hn
        item = (fn, count, current)
        self.que.put(item) 

        #set to priority queue and store initial state in a search set
        tupleState = tuple(map(tuple, current.state))
        self.explored.add(tupleState)

        while not (self.que.empty()):
            #set queue size to maximum
            self.maxQ = max(maxQ, self.que.qsize())


            #(current_fn, current_count, current_current) = self.que.get()
            first = self.que.get()
            current = first[2]
            tupleState = tuple(map(tuple, current.state)) #[[1, 2][3, 4]] turn it to ((1, 2), (3, 4))
            self.explored.add(tupleState)

             # printing
            hn = heuristic(current.state, self.goalState)
            print("The best state to expand with g(n) = {} and h(n) = {} is...".format(current.gn, hn))
            self.printPuzzle(current.state)
            print("Expanding this node...")
            print('--------')


            #check if it match the goal,
            if current.state == self.goalState:
                self.nodesSearched = nodeNum 
                self.findSolutionPath(current)
                self.printGoalMes()
                self.PrintSolutionPath()
                return

            # all possible next moves
            pMoves = current.getMoves()

            for node in pMoves:
                count += 1
                tupleState = tuple(map(tuple, node.state))
                if tupleState not in self.explored:
                    node.parent = current
                    hn = heuristic(node.state, self.goalState)
                    fn = node.gn + hn
                    item = (fn, count, node)
                    self.que.put(item)

            nodeNum += 1
        return 
      

    #performs the A* Misplaced Tile heuristic search
    def AStarTile(self):
       self.AStarSearch(self.numberMisplacedTile)



    #performs the A* Euclidean distance heuristic 
    def AStarDist(self):
        self.AStarSearch(self.distMisplacedTile)


    #count the number of misplaced tile
    def numberMisplacedTile(self, state, goal):
        count =0
        for r in range(len(state)):
            for c in range(len(state[r])):
                if (state[r][c] != self.goalState[r][c] and state[r][c] !=0):
                    count+=1
        return count
    
    #calculate the distance between current state and a goal state tile. 
    #Euclidean distance = sqrt()
    def distMisplacedTile(self, state, goal):
        distance = 0

        #initailize hashmap to keep track on goal coordinates
        # key is state number : value is [row, col]
        goalMap = {}
        for i in range(len(goal)):
            for j in range(len(goal[0])):
                goalMap[goal[i][j]] = [i, j]
        
        #calculate euclidean distance
        for r in range(len(state)):
            for c in range(len(state[0])):
                #skip 0
                if state[r][c] == 0:
                    continue
                goal_row, goal_col = goalMap[state[r][c]]
                distance += math.sqrt((r-goal_row)**2 +(c -goal_col)**2)


        return round(distance)
    
    def EuclideanDistance(self, puzzle):
        EuclideanDistanceTotal = 0
        for r in range(len(puzzle)): #go through the puzzle, checking if the number is in the right place
            for c in range(len(puzzle)):
                if puzzle[r][c] != (r+1)*len(puzzle)+(c+1):
                    if puzzle[r][c] == 0:
                        ProperPosY = len(puzzle)
                        ProperPosX = len(puzzle)
                    else:
                        ProperPosY = int(puzzle[r][c]/len(puzzle)) #get the proper position of the number
                        ProperPosX = puzzle[r][c]-ProperPosY
                    EuclideanDistanceTotal += math.sqrt((r-ProperPosY)**2+(c-ProperPosX)**2)

        return EuclideanDistanceTotal
