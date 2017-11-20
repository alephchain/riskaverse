from agent import *
from payoff import *

agent = Agent(RISK_AVERSE)

payoff(agent)

print agent.get_score()

