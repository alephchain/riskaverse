from utility import *


class Agent:

    def __init__(self, idx, strategy):
        self._id = idx
        self.score = []
        self.strategy = strategy

    def set_score(self, payoff):
        self.score.append(payoff)

    def get_score(self):
        sum_score = 0
        for i in range(len(self.score)-1):
            sum_score += self.score[i]

        return sum_score

    def strategy_label(self):
        return get_strategy(self.strategy)
