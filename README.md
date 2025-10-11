# The Eight Puzzle
CS 170 Project1 

## Overview 
This project demonstrate the use of Search algorithm to sovle 8 puzzle by using 3 search algorithm: 
* Uniform Cost Search - BFS
* A* with the Misplaced Tile heuristic
* A* with the Euclidean Distance heuristic

## Tool and Technologies: 
* Python - terminal base interface
* In terminal, run the program with python main.py

## Initial Plan
We are going to use tree class and node class to make each state. Each node can have upto 4 children and are limited by the moves which we can define by checking the limits first. 

## The node and tree class
The node needs to keep track of the state of the puzzle and nothing else in the state. 
The tree class will keep track of the depth, the maximum amount of nodes in the queue in the program, and the number of nodes that were created in the whole process "number of nodes in the tree".

## Run Time:
Using python build in Time by start at the begining of each search and record until it end. The print statement show the period for each search. 
Used Defualt Puzzle, to measure the estimate different search algorithm. 
* Uniform Cost Search : 0.0208 seconds.
* A* with the Misplaced Tile heuristic: 0.0042 seconds.
* A* with the Euclidean Distance heuristic: 0.0045 seconds.
From the USC to A*, it improves run time by 78%. 
