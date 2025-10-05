import random

QUOTES = [
    "Push yourself, because no one else is going to do it for you.",
    "Success is the sum of small efforts repeated daily.",
    "Don’t watch the clock; do what it does. Keep going.",
    "You’ve got this. One page at a time."
]

def get_motivational_quote():
    return random.choice(QUOTES)
