# multiAgents.py
# --------------
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
from math import inf
from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # Get the position of the ghosts
        newGhostPositions = successorGameState.getGhostPositions()

        """
        Calculate the distance from the new pacman's position
        to the nearest food and then reverse it if it isn't zero
        """
        foodScore = 0 if (len(newFood.asList()) == 0) else float(
            min([util.manhattanDistance(newPos, foodPos) for foodPos in newFood.asList()]))
        if foodScore != 0:
            foodScore = 1 / foodScore

        """
        Calculate the distance from the new pacman's position
        to the nearest ghost and  if this distance is less
        then 2 then we set it to -infinite
        """
        ghostScore = 0
        closestGhost = min([util.manhattanDistance(newPos, ghostPos) for ghostPos in newGhostPositions])
        if closestGhost < 2:
            ghostScore = -inf

        """
        Calculate the score gained from this movement
        """
        actionScore = successorGameState.getScore() - currentGameState.getScore()
        return actionScore + foodScore + ghostScore


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        """
        This function calculates the best choice for the 
        max nodes and returns the best score and it's correspond action
        """
        def maxValue(state, depth, agentIndex):
            depth -= 1
            if depth < 0 or state.isLose() or state.isWin():
                return None, self.evaluationFunction(state)
            value = -inf
            legalActions = state.getLegalActions(agentIndex)
            for action in legalActions:
                tempNext = state.generateSuccessor(agentIndex, action)
                score = minValue(tempNext, depth, agentIndex + 1)[1]
                if score > value:
                    value = score
                    maxAction = action
            return maxAction, value

        """
        This function calculates the best choice for the 
        min nodes and returns the best score and it's correspond action
        """
        def minValue(state, depth, agentIndex):
            if state.isLose() or state.isWin():
                return None, self.evaluationFunction(state)
            value = +inf
            (function, nextAgent) = (minValue, agentIndex + 1) if agentIndex < state.getNumAgents() - 1 else (
            maxValue, 0)
            legalActions = state.getLegalActions(agentIndex)
            for action in legalActions:
                tempNext = state.generateSuccessor(agentIndex, action)
                score = function(tempNext, depth, nextAgent)[1]
                if score < value:
                    value = score
                    minAction = action
            return minAction, value

        return maxValue(gameState, self.depth, 0)[0]


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def maxValue(state, depth, agentIndex, alpha, beta):
            depth -= 1
            if depth < 0 or state.isLose() or state.isWin():
                return None, self.evaluationFunction(state)
            value = -inf
            legalActions = state.getLegalActions(agentIndex)
            for action in legalActions:
                tempNext = state.generateSuccessor(agentIndex, action)
                score = minValue(tempNext, depth, agentIndex + 1, alpha, beta)[1]
                if score > value:
                    value = score
                    maxAction = action
                if value > beta:
                    return maxAction, value
                alpha = max(alpha, value)
            return maxAction, value

        def minValue(state, depth, agentIndex, alpha, beta):
            if state.isLose() or state.isWin():
                return None, self.evaluationFunction(state)
            value = +inf
            (function, nextAgent) = (minValue, agentIndex + 1) if agentIndex < state.getNumAgents() - 1 else (
                maxValue, 0)
            legalActions = state.getLegalActions(agentIndex)
            for action in legalActions:
                tempNext = state.generateSuccessor(agentIndex, action)
                score = function(tempNext, depth, nextAgent, alpha, beta)[1]
                if score < value:
                    value = score
                    minAction = action
                if value < alpha:
                    return minAction, value
                beta = min(beta, value)
            return minAction, value

        return maxValue(gameState, self.depth, 0, -inf, +inf)[0]


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        def maxValue(state, depth, agentIndex):
            depth -= 1
            if depth < 0 or state.isLose() or state.isWin():
                return None, self.evaluationFunction(state)
            value = -inf
            legalActions = state.getLegalActions(agentIndex)
            for action in legalActions:
                tempNext = state.generateSuccessor(agentIndex, action)
                score = expectedValue(tempNext, depth, agentIndex + 1)[1]
                if score > value:
                    value = score
                    maxAction = action
            return maxAction, value

        def expectedValue(state, depth, agentIndex):
            if state.isLose() or state.isWin():
                return None, self.evaluationFunction(state)
            (function, nextAgent) = (expectedValue, agentIndex + 1) if agentIndex < state.getNumAgents() - 1 else (
                maxValue, 0)
            legalActions = state.getLegalActions(agentIndex)
            summation = 0
            for action in legalActions:
                tempNext = state.generateSuccessor(agentIndex, action)
                score = function(tempNext, depth, nextAgent)[1]
                summation += score
            finalScore = summation / len(legalActions)
            return None, finalScore

        return maxValue(gameState, self.depth, 0)[0]


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    # Calculate the score of the current state
    scorePosition = currentGameState.getScore()

    # Calculate the summation of distances from all the foods
    position = currentGameState.getPacmanPosition()
    foodList = currentGameState.getFood().asList()
    totalFoodDistance = 1
    if len(foodList) != 0:
        for temp in foodList:
            totalFoodDistance += manhattanDistance(position, temp)

    # Calculate the total scared times of all the ghosts
    ghostStates = currentGameState.getGhostStates()
    ghostScaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]
    ghostScaredTimeSum = 0
    if len(ghostStates) != 0:
        for temp in ghostScaredTimes:
            ghostScaredTimeSum += temp

    # Calculate the summation of distances from all the ghosts
    ghostPositions = currentGameState.getGhostPositions()
    totalGhostDistance = 0
    for temp in ghostPositions:
        totalGhostDistance += util.manhattanDistance(position, temp)

    evaluation = 1.0 / totalFoodDistance + scorePosition + ghostScaredTimeSum + totalGhostDistance
    return evaluation


# Abbreviation
better = betterEvaluationFunction
