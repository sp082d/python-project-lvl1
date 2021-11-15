# -*- coding: utf-8 -*-

"""Brain GCD game functions."""


import math
from brain_games.games.common import generate_number


def make_question():
    """Generate game question."""
    num1 = generate_number()
    num2 = generate_number()
    question = 'Question: {first_num} {second_num}'.format(first_num=num1, second_num=num2)
    answer = math.gcd(num1, num2)
    return question, str(answer)
