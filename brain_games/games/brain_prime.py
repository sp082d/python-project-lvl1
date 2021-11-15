# -*- coding: utf-8 -*-

"""Brain prime game functions."""


import math
from brain_games.games.common import generate_number


def is_prime(number):
    """Check if number is prime or not."""
    if number < 2 < number:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    else:
        return True


def make_question():
    """Generate game question."""
    number = generate_number()
    question = 'Question: {number}'.format(number=number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer
