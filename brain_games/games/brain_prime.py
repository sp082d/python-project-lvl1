# -*- coding: utf-8 -*-

"""Brain prime game functions."""


from brain_games.game_engine import generate_number


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Check if number is prime or not."""
    if number in [2, 3]:
        return True
    if number % 2 == 0 or number < 2:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    else:
        return True


def make_question():
    """Generate game question."""
    number = generate_number()
    question = f'Question: {number}'
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer
