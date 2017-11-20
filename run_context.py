from random import randint

from agent import *
from payoff import *

agents = []
for i in range(400):
    agents.append(Agent(i, randint(0, 3)))
    payoff(agents[i])
    print agents[i].get_score()

