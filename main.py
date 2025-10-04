from Search import *

#asks user for their choice in puzzzle
def main():
    while True:
        try:
            print("Welcome to abell062, ltain005, and gwang0868 puzzle solver. Choose one of the options:")
            print("1 for default puzzle.")
            print("2 to enter your own puzzle.")

            choice = input("Your choice is: ")

            if choice == '1':
                #create a default puzzle and run a search algorithm. 
                puzzleSize = 3
                defaultPuzzle = [[1, 2, 3], [4, 8, 0], [7, 6, 5]]
                problem = Problem(defaultPuzzle, puzzleSize)
                searchChoice(problem)
                break

            #user input puzzle and choose a size. 
            elif choice == '2':
                while True:
                    try:
                        puzzleSize = int(input("Enter the puzzle size (number only [ex. 5]): "))
                        checkUserInput(puzzleSize, 2)
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
            else:
                print("Invalid choice. Please select 1 or 2.")
        except ValueError:
            print("The input provided is not valid. Please try again.")

        #exit a program 
        inputUser = input("would you like to solve another puzzle?\n Y for yes, any key to stop: ")
        if inputUser.lower() != 'y':
            print("Exit the program. \n")
            break

#check if the user iput for their own puzzle is within the limits
def checkUserInput(puzzleSize, choice):
    puzzle = []
    numberSet = set()
    restartCheck = True

    #Lyda: should we consider using while loop instead of recursive for memomry efficiency. 1
    for i in range(puzzleSize):
        row = input(f"Please enter row {i+1} values (space-separated, e.g., '1 2 3'): ")
        row = row.strip().split()

        #check if each row input is the same size. 
        if len(row) != puzzleSize:
            print("Incorrect number of entries. Please start over.")
            restartCheck = False
            break

        intRow = []
        for i, item in enumerate(row):
                try:
                    item_int = int(item)

                    #check if the input is in range from 0 to size^2
                    if item_int < 0 or item_int >= puzzleSize ** 2:
                        print(f"Value out of range: {item_int}")
                        restartCheck = False
                        break
                    
                    #check if the input is not duplicate
                    if item_int in numberSet:
                        print(f"Duplicate value: {item_int}")
                        restartCheck = False
                        break
                    
                    #add to nunmberSet for checking duplucate
                    #inRow for each row. 
                    numberSet.add(item_int)
                    intRow.append(item_int)

                except ValueError:
                    print(f"Invalid input, not an integer: {item}")
                    restartCheck = False
                    break

        if not restartCheck:
            break

        puzzle.append(intRow)

    if not restartCheck:
        print("Invalid row input detected. Restarting input process...")
        checkUserInput(puzzleSize, choice)
        return
    
    problem = Problem(puzzle, puzzleSize)
    searchChoice(problem)

#asks user for their choice of search
def searchChoice(problem):
    while True:
        try:
            print("Enter your choice of algorithm: \n (1) Uniform Cost Search \n (2) A* with the Misplaced Tile heuristic. \n (3) A* with the Euclidean distance heuristic.")
            search = int(input("What is your choice: "))
            if search == 1:
                problem.UniCostSearch()
                return
            elif search == 2:
                problem.AStarTile()
                return
            elif search == 3:
                problem.AStarDist()
                return
            else:
                print("Invalid input. Please enter number 1 or 2 or 3.")
        except ValueError:
            print("Invalid input. Please enter number 1 or 2 or 3.")
    
#running the whole program in the loop
if __name__ == "__main__":
    main()
