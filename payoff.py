from random import randint
from constants import *


def payoff(agent):
    if agent.is_active():
        active_strategy = agent.strategy

        outcome = outcomes(agent.odds)
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
            if active_strategy == BUY_AND_HOLD:
                reward_outcome = randint(0, 1)
                if reward_outcome == 0:
                    reward = 0
                else:
                    reward = 10
        else: # outcome == LOSE:
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
            if active_strategy == BUY_AND_HOLD:
                reward_outcome = randint(0, 1)
                if reward_outcome == 0:
                    reward = 0
                else:
                    reward = -10

        agent.set_score(reward)

    return agent


def outcomes(odds):
    percentage = randint(0, 2)

    if odds == TWENTY_FIVE:
        if percentage == 0:
            return WIN
        else:
            return LOSE
    elif odds == FIFTY:
        return randint(0, 1)
    elif odds == SEVENTY_FIVE:
        if percentage >= 1:
            return WIN
        else:
            return LOSE
    elif odds == RANDOM:
        return outcomes(randint(0, 2))
