from random import randint
from constants import *


def payoff(agent):
    if agent.is_active():
        active_strategy = agent.strategy

        outcome = randint(0, 1)
        reward = 0
        if outcome == WIN:
            if active_strategy == RISK_AVERSE:
                reward = 10
            if active_strategy == RISK_TAKING:
                reward_outcome = randint(0, 1)
                if reward_outcome == 0:
                    reward = 0
                else:
                    reward = 20
            if active_strategy == CONSERVATIVE:
                reward = 10
            if active_strategy == BUY_AND_HOLD:
                reward_outcome = randint(0, 1)
                if reward_outcome == 0:
                    reward = 0
                else:
                    reward = 20
        elif outcome == LOSE:
            if active_strategy == RISK_AVERSE:
                reward_outcome = randint(0, 1)
                if reward_outcome == 0:
                    reward = 0
                else:
                    reward = -20
            if active_strategy == RISK_TAKING:
                reward = -10
            if active_strategy == CONSERVATIVE:
                reward = -10
            if active_strategy == BUY_AND_HOLD:
                reward_outcome = randint(0, 1)
                if reward_outcome == 0:
                    reward = 0
                else:
                    reward = -20

        agent.set_score(reward)

    return agent
