# -*- coding: utf-8 -*-

"""Functions common to all games."""


from random import randint


def generate_number():
    """Return random number from range."""
    return randint(1, 10)


def check_answer(user_answer, correct_answer):
    """Check users answer."""

    if user_answer == correct_answer:
        message = 'Correct!'
        return True, message

    message = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
    return False, message.format(wrong=user_answer, correct=correct_answer)
