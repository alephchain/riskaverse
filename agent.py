from utility import *


class Agent:

    def __init__(self, idx, odds, strategy):
        self.idx = idx
        self.score = []
        self.strategy = strategy
        self.odds = odds
        self.returns = 1000

    def set_score(self, payoff):
        new_return = self.returns + payoff
        if new_return < 0:
            self.score.append(0)
            self.returns = 0
        else:
            self.score.append(payoff)
            self.returns = new_return

    def get_age(self):
        age = 0
        sum_score = 1000
        for i in self.score:
            age += 1
            sum_score += self.score[i]
            if sum_score == 0:
                return age

        return age

    def get_score(self):
        return self.returns

    def strategy_label(self):
        return get_strategy(self.strategy)

    def is_active(self):
        return self.returns > 0

    def odds_label(self):
        return get_odds(self.odds)