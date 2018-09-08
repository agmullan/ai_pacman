from game import Agent
from game import Directions
from game import Configuration
import random;

class DumbAgent(Agent):
    "An agent that goes West until it can't."
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print("Location:", state.getPacmanPosition())
        print("Action available:", state.getLegalPacmanActions())
        if Directions.WEST in state.getLegalPacmanActions():
            print("Going West.")
            return Directions.WEST
        else:
            print("Stopping.")
            return Directions.STOP
#"The agent always goes West. "
#return Directions.WEST
class RandomAgent(Agent):
    "An agent that choices a random direction and move until you hit wall then choose different direction"
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print("Location:", state.getPacmanPosition())
        print("Action available:", state.getLegalPacmanActions())

        if len(state.getLegalPacmanActions()) > 0:
            print("list full")
            secure_random = random.SystemRandom()
            randomDirection = secure_random.choice(state.getLegalPacmanActions())
            print(randomDirection)
            return randomDirection
        else:
            print("list empty")
        return Directions.STOP
