
class Agent:

    def __init__(self, strategy):
        self.score = 0
        self.strategy = strategy

    def set_score(self, payoff):
        self.score += payoff

    def get_score(self):
        return self.score


