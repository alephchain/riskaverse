from random import randint
from constants import *
import csv

from agent import *
from payoff import *

max_agents = 400
strategies = 4
odds_calc = 4
steps = (2 ** 12)

agents = []

for i in range(max_agents * odds_calc):
    agents.append(Agent(i, i % odds_calc, i % strategies))

for i in range(steps * max_agents * odds_calc):
    agent_idx = i % (max_agents * odds_calc)
    payoff(agents[agent_idx])

with open(r'C:\Users\gutzofter\PycharmProjects\riskaverse\data\strategy.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['strategy', 'odds', 'score'])

    for i in range(max_agents * odds_calc):
        print agents[i].idx, agents[i].strategy_label(), agents[i].odds_label(), agents[i].get_score()
        writer.writerow([agents[i].strategy_label(), agents[i].odds_label(), agents[i].get_score()])

print "Agents: " + str(max_agents * odds_calc), "Steps: " + str(steps)
