# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    # Stores location of each node
    fringe = util.Stack()
    # Stores path to each node (correspond to the nodes in fringe)
    path = util.Stack()
    # Sets the start node's location
    startLocation = problem.getStartState()
    # Pushes the start node's location to the fringe
    fringe.push(startLocation)
    # Pushes the start node's path to the fringe which in empty
    path.push([])
    # Stores the locations pacman explored
    exploredLocations = list()

    while not fringe.isEmpty():
        # Pop a node's location from top of the stack
        nodeLocation = fringe.pop()
        # Pop corresponding node's path from top of the stack
        nodePath = path.pop()
        exploredLocations.append(nodeLocation)
        # Goal test
        if problem.isGoalState(nodeLocation):
            return nodePath
        # Get the successors of the under review node
        successors = problem.getSuccessors(nodeLocation)
        for temp in successors:
            if temp[0] not in exploredLocations:
                fringe.push(temp[0])
                path.push(nodePath + [temp[1]])
    return None



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    # Stores location of each node
    fringe = util.Queue()
    # Stores path to each node (correspond to the nodes in fringe)
    path = util.Queue()
    # Sets the start node's location
    startLocation = problem.getStartState()
    # Pushes the start node's location to the fringe
    fringe.push(startLocation)
    # Pushes the start node's path to the fringe which in empty
    path.push([])
    # Stores the locations pacman explored
    exploredLocations = list()
    # Adds the start node's location as explored
    exploredLocations.append(startLocation)

    while not fringe.isEmpty():
        # Pop a node's location from top of the stack
        nodeLocation = fringe.pop()
        # Pop corresponding node's path from top of the stack
        nodePath = path.pop()
        # Goal test
        if problem.isGoalState(nodeLocation):
            return nodePath
        # Get the successors of the under review node
        successors = problem.getSuccessors(nodeLocation)
        for temp in successors:
            if temp[0] not in exploredLocations:
                fringe.push(temp[0])
                path.push(nodePath + [temp[1]])
                exploredLocations.append(temp[0])
    return None


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    # Stores location of each node and its cost
    fringe = util.PriorityQueue()
    # Stores path to each node (correspond to the nodes in fringe)
    path = util.PriorityQueue()
    # Sets the start node's location
    startLocation = problem.getStartState()
    # Pushes the start node's location to the fringe
    # and its cost which is 0
    fringe.push((startLocation, 0), 0)
    # Pushes the start node's path to the fringe which in empty
    path.push([], 0)
    # Stores the locations pacman explored
    exploredLocations = list()

    while not fringe.isEmpty():
        # Pop a node's location and cost from top of the stack
        nodeLocationAndCost = fringe.pop()
        # Pop corresponding node's path from top of the stack
        nodePath = path.pop()
        # Goal test
        if problem.isGoalState(nodeLocationAndCost[0]):
            return nodePath
        if nodeLocationAndCost[0] not in exploredLocations:
            exploredLocations.append(nodeLocationAndCost[0])
            # Get the successors of the under review node
            successors = problem.getSuccessors(nodeLocationAndCost[0])
            for temp in successors:
                if temp[0] not in exploredLocations:
                    cost = temp[2] + nodeLocationAndCost[1]
                    fringe.push((temp[0], cost), cost)
                    path.push(nodePath + [temp[1]], cost)

    return None


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Priority for this problem is the sum of heuristic and backward cost
    # Stores location of each node and its cost
    fringe = util.PriorityQueue()
    # Stores path to each node (correspond to the nodes in fringe)
    path = util.PriorityQueue()
    # Sets the start node's location
    startLocation = problem.getStartState()
    # Pushes the start node's location to the fringe
    # and its cost which is 0
    fringe.push((startLocation, 0), 0)
    # Pushes the start node's path to the fringe which in empty
    path.push([], 0)
    # Stores the locations pacman explored
    exploredLocations = list()

    while not fringe.isEmpty():
        # Pop a node's location and cost from top of the stack
        nodeLocationAndCost = fringe.pop()
        # Pop corresponding node's path from top of the stack
        nodePath = path.pop()
        # Goal test
        if problem.isGoalState(nodeLocationAndCost[0]):
            return nodePath
        if nodeLocationAndCost[0] not in exploredLocations:
            exploredLocations.append(nodeLocationAndCost[0])
            # Get the successors of the under review node
            successors = problem.getSuccessors(nodeLocationAndCost[0])
            for temp in successors:
                if temp[0] not in exploredLocations:
                    cost = temp[2] + nodeLocationAndCost[1]
                    totalCost = heuristic(temp[0], problem) + cost
                    fringe.push((temp[0], cost), totalCost)
                    path.push(nodePath + [temp[1]], totalCost)

    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
