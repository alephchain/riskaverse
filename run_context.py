from random import randint
from constants import *
from agent import *
from payoff import *

agents = []
for i in range(400):
    agents.append(Agent(i, randint(0, 3)))

for i in range(2 ** 16):
    agent_idx = i % 400
    payoff(agents[agent_idx])

    active_strategy = agents[agent_idx].strategy

    print agents[agent_idx].strategy_label(), agents[agent_idx].get_score()
