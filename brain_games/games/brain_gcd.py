# -*- coding: utf-8 -*-

"""Brain GCD game functions."""

from typing import Tuple
from brain_games.game_engine import generate_number


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question() -> Tuple[str, str]:
    """Generate game question."""
    num1 = generate_number()
    num2 = generate_number()

    return f'Question: {num1} {num2}', str(gcd(num1, num2))


def gcd(num1: int, num2: int) -> int:
    """Return GCD of two numbers."""
    if not num2:
        return num1
    else:
        return gcd(num2, num1 % num2)
