# The Eight Puzzle
CS 170 Project1 

## Overview 
This project demonstrate the use of Search algorithm to sovle 8 puzzle by using 3 search algorithm: 
* Uniform Cost Search - BFS
* A* with the Misplaced Tile heuristic
* A* with the Euclidean Distance heuristic

## Tool and Technologies: 
* Python - terminal base interface

## Initial Plan
We are going to use tree class and node class to make each state. Each node can have upto 4 children and are limited by the moves which we can define by checking the limits first. 

## The node and tree class
The node needs to keep track of the state of the puzzle and nothing else in the state. 
The tree class will keep track of the depth, the maximum amount of nodes in the queue in the program, and the number of nodes that were created in the whole process "number of nodes in the tree".
