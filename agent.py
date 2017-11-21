from constants import *


class Agent:

    def __init__(self, idx, strategy):
        self._id = idx
        self.score = 0
        self.strategy = strategy

    def set_score(self, payoff):
        self.score += payoff

    def get_score(self):
        return self.score

    def strategy_label(self):
        if self.strategy == RISK_AVERSE:
            return "RISK_AVERSE"

        if self.strategy == RISK_TAKING:
            return "RISK_TAKING"

        if self.strategy == CONSERVATIVE:
            return "CONSERVATIVE"

        if self.strategy == WILD:
            return "WILD"
