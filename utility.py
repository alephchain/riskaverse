from constants import *


def get_strategy(strategy):
    if strategy == RISK_AVERSE:
        return "RISK_AVERSE"

    if strategy == RISK_TAKING:
        return "RISK_TAKING"

    if strategy == CONSERVATIVE:
        return "CONSERVATIVE"

    if strategy == WILD:
        return "WILD"