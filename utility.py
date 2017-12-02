from constants import *


def get_strategy(strategy):
    if strategy == RISK_AVERSE:
        return "RISK_AVERSE"

    if strategy == RISK_TAKING:
        return "RISK_TAKING"

    if strategy == CONSERVATIVE:
        return "CONSERVATIVE"

    if strategy == BUY_AND_HOLD:
        return "BUY_AND_HOLD"


def get_odds(odds):
    if odds == TWENTY_FIVE:
        return "TWENTY_FIVE"
    if odds == FIFTY:
        return "FIFTY"
    if odds == SEVENTY_FIVE:
        return "SEVENTY_FIVE"
    if odds == RANDOM:
        return "RANDOM"

