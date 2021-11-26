# -*- coding: utf-8 -*-

"""Brain GCD game functions."""


from brain_games.game_engine import generate_number


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question():
    """Generate game question."""
    num1 = generate_number()
    num2 = generate_number()
    question = f'Question: {num1} {num2}'
    return question, str(gcd(num1, num2))


def gcd(num1, num2):
    """Return GCD of two numbers."""
    if not num2:
        return num1
    else:
        return gcd(num2, num1 % num2)
