from random import randint
from constants import *
import csv

from agent import *
from payoff import *

max_agents = 4000
steps = (2 ** 16)

agents = []
for i in range(max_agents):
    agents.append(Agent(i, i % 4))

for i in range(steps * max_agents):
    agent_idx = i % max_agents
    payoff(agents[agent_idx])

with open(r'C:\Users\owner\PycharmProjects\riskaverse\data\strategy.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['strategy', 'score'])

    for i in range(max_agents):
        print agents[i].strategy_label(), agents[i].get_score()
        writer.writerow([agents[i].strategy_label(), agents[i].get_score()])

print "Agents: " + str(max_agents), "Steps: " + str(steps)
