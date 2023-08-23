# Pac-Man-AI
The Pac-Man projects were developed for UC Berkeley's introductory artificial intelligence course. These projects cover three main topics in artificial intelligence: search, multiagents, and reinforcement learning. In each folder, there is a .zip file that holds the original files of the project, and there are some .py files that contain the answers to each scenario. You can use the original files and solve the problem to measure your knowledge and use the answers if needed. Feel free to try different implementations for each scenario. Here is a summary of each issue.

# Search
![ezgif com-crop](https://github.com/Mohadeseh-Atyabi/Pac-Man-AI/assets/72689599/be3c5a14-589c-4ae2-8141-ea24cfda4126)


Pac-Man lives in a shiny blue world of winding corridors and delicious food. Optimum movement in this world is Pac-Man's first step to success in this world. There are different scenarios in this project to aim the goal of optimizing the Pac-Man's movement:
- Find the fixed point using BFS
- Implementation of DFS
- Changing the cost function
- A star search
- Finding all the corners
- Changing the heuristic function to a non-trivial and consistent one
- Eating all the dots
- Suboptimal search

The suggested answers are in the [search](https://github.com/Mohadeseh-Atyabi/Pac-Man-AI/tree/main/search) directory.

# Multiagents
![ezgif com-crop(1)](https://github.com/Mohadeseh-Atyabi/Pac-Man-AI/assets/72689599/922223ce-d603-488d-8e8c-39018ad1cead)


In this project, you will design an agent for the classic Pa-Mman game, which, this time, also includes ghosts. In this path, you will use minimax search and expectimax and design the evaluation function.
- Reflect agent: The goal is to change the evaluation function so it uses the result of the action and the secondary state to do the evaluation
- Minimax
- Alpha-Beta pruning
- Expectimax
- Evaluation function: This function should evaluate the states instead of the action

The suggested answers exist in the [multiagent](https://github.com/Mohadeseh-Atyabi/Pac-Man-AI/tree/main/multiagents) directory.

# Reinforcement learning
![ezgif com-crop (1)](https://github.com/Mohadeseh-Atyabi/Pac-Man-AI/assets/72689599/caadf33b-f2e8-4abd-843d-c175cbc86cb9)


In this project, you will implement value iteration and Q-learning. First, you will evaluate your agents in Gridworld and then, apply that on a simulated robot, called Crawler, and the Pac-Man. Here, you can run the gridworld.py in mannual state and use the arrow keys to move on the space. Remember that if you press the up key, the agents obey it in 80% of the time.
- Value iteration
- Bridge crossing analysis
- Policies
- Asynchronous value iteration
- Prioritized sweeping value iteration
- Q-learning
- Greedy epsilon
- Pac-Man and Q-learning

The suggested answers exist in the [reinforcement learning](https://github.com/Mohadeseh-Atyabi/Pac-Man-AI/tree/main/reinforcement%20learning) directory.
