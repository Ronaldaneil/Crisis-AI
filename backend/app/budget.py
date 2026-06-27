"""
budget.py

Tracks AI usage cost and remaining budget.
"""

TOTAL_BUDGET = 2.00      # $2 Hackathon Budget
remaining_budget = TOTAL_BUDGET


def check_budget(cost: float):
    """
    Checks if enough budget remains.
    """

    global remaining_budget

    if remaining_budget >= cost:

        remaining_budget -= cost

        return {
            "allowed": True,
            "remaining_budget": round(remaining_budget, 3)
        }

    return {
        "allowed": False,
        "remaining_budget": round(remaining_budget, 3)
    }


def get_remaining_budget():

    return round(remaining_budget, 3)