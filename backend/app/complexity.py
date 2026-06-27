"""
complexity.py
Calculates how complex a disaster request is.
"""

HIGH_COMPLEXITY = [
    "injured",
    "trapped",
    "bleeding",
    "medical",
    "evacuation",
    "family",
    "children",
    "grandmother",
    "grandfather",
    "flood",
    "earthquake",
    "fire",
    "collapsed",
    "multiple",
    "route",
    "safe route"
]

MEDIUM_COMPLEXITY = [
    "shelter",
    "location",
    "help",
    "emergency",
    "gps",
    "navigate"
    "Water"
    "Food"
]


def calculate_complexity(prompt: str):

    score = 1

    text = prompt.lower()

    for word in MEDIUM_COMPLEXITY:
        if word in text:
            score += 1

    for word in HIGH_COMPLEXITY:
        if word in text:
            score += 2

    return min(score, 10)