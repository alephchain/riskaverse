from random import randint

from agent import *


WIN = 1
LOSE = 0

RISK_AVERSE = 0
RISK_TAKING = 1
CONSERVATIVE = 2
WILD = 3


def payoff(agent):
    active_strategy = agent.strategy()

    outcome = randint(0, 1)
    reward = 0
    if outcome == WIN:
        if active_strategy == RISK_AVERSE:
            reward = 5
        if active_strategy == RISK_TAKING:
            reward_outcome = randint(0, 1)
            if reward_outcome == 0:
                reward = 0
            else:
                reward = 10
        if active_strategy == CONSERVATIVE:
            reward = 5
        if active_strategy == WILD:
            reward_outcome = randint(0, 1)
            if reward_outcome == 0:
                reward = 0
            else:
                reward = 10
    else:
        if active_strategy == RISK_AVERSE:
            reward_outcome = randint(0, 1)
            if reward_outcome == 0:
                reward = 0
            else:
                reward = -10
        if active_strategy == RISK_TAKING:
            reward = -5
        if active_strategy == CONSERVATIVE:
            reward = -5
        if active_strategy == WILD:
            reward_outcome = randint(0, 1)
            if reward_outcome == 0:
                reward = 0
            else:
                reward = -10

    agent.set_score(reward)

    return agent
