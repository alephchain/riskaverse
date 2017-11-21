from utility import *


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
        return get_strategy(self.strategy)
