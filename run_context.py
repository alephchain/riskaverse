from random import randint
from constants import *
import csv

from agent import *
from payoff import *

max_agents = 1000
strategies = 4
odds_calc = 4
steps = (2 ** 12)


agents = []

i = 0
for a in range(max_agents):
    for o in range(odds_calc):
        for s in range(strategies):
            agents.append(Agent(i, o, s))
            i += 1

for i in range(steps * max_agents * odds_calc * strategies):
    agent_idx = i % (max_agents * odds_calc * strategies)
    payoff(agents[agent_idx])

with open(r'C:\Users\owner\PycharmProjects\riskaverse\data\strategy.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['index', 'strategy', 'age', 'odds', 'score'])

    for i in range(max_agents * odds_calc * strategies):
        print agents[i].idx, agents[i].get_age(), agents[i].strategy_label(), agents[i].odds_label(), agents[
            i].get_return()
        writer.writerow([agents[i].idx, agents[i].strategy_label(), agents[i].get_age(), agents[i].odds_label(),
                         agents[i].get_return()])

with open(r'C:\Users\owner\PycharmProjects\riskaverse\data\agents.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['index', 'strategy', 'age', 'odds', 'returns', 'seq', 'score'])

    for agent in agents:
        seq = 0
        for score in agent.get_score():
            writer.writerow([agent.idx, agent.strategy_label(), agent.get_age(), agent.odds_label(), agent.get_return(), seq, score])
            seq += 1

print "Agents: " + str(max_agents * odds_calc * strategies), "Steps: " + str(steps)
