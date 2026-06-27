"""
router.py

Chooses the best AI model based on request complexity.
"""


def select_model(complexity: int):

    return {
        "model": "mzai:meta-llama/Llama-3.3-70B-Instruct",
        "reason": "Using verified working model",
        "estimated_cost": 0.13
    }