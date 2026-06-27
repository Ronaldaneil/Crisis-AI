"""
router.py

Chooses the best AI model based on request complexity.
"""


def select_model(complexity: int):

    if complexity <= 3:
        return {
            "model": "mzai:google/Gemma-2-2b-it",
            "reason": "Simple request",
            "estimated_cost": 0.02
        }

    elif complexity <= 6:
        return {
            "model": "mzai:qwen/Qwen3-30B-A3B-Instruct-2507",
            "reason": "Moderately complex request",
            "estimated_cost": 0.10
        }

    else:
        return {
            "model": "mzai:meta-llama/Llama-3.3-70B-Instruct",
            "reason": "High complexity disaster request",
            "estimated_cost": 0.13
        }