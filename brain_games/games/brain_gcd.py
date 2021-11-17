# -*- coding: utf-8 -*-

"""Brain GCD game functions."""


import math
from brain_games.game_engine import generate_number


def make_question():
    """Generate game question."""
    num1 = generate_number()
    num2 = generate_number()
    question = f'Question: {num1} {num2}'
    answer = math.gcd(num1, num2)
    return question, str(answer)
