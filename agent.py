from utility import *


class Agent:

    def __init__(self, idx, strategy):
        self._id = idx
        self.score = []
        self.strategy = strategy
        self.returns = 1000

    def set_score(self, payoff):
        self.returns -= 5
        new_return = self.returns + payoff
        if new_return < 0:
            self.score.append(0)
            self.returns = 0
        else:
            self.score.append(payoff)
            self.returns = new_return

    def get_score(self):
        return self.returns

    def strategy_label(self):
        return get_strategy(self.strategy)

    def is_active(self):
        return self.returns > 0
