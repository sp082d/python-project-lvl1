# -*- coding: utf-8 -*-

"""Brain prime game functions."""

from typing import Tuple
from brain_games.game_engine import generate_number


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
UP_TO_2_DIGITS = 99


def make_question() -> Tuple[str, str]:
    """Generate game question."""
    number = generate_number(end=UP_TO_2_DIGITS)
    return f'Question: {number}', \
           'yes' if is_prime(number) else 'no'


def is_prime(number: int) -> bool:
    """Check if number is prime or not."""
    if number in [2, 3]:
        return True
    elif number % 2 == 0 or number == 1:
        return False
    else:
        for divisor in range(3, int(number ** 0.5) + 1, 2):
            if number % divisor == 0:
                return False
        else:
            return True
