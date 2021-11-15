# -*- coding: utf-8 -*-

"""Brain even game functions."""

from random import randint


def generate_number():
    """Generate random number."""
    return randint(1, 100)


def check_answer(user_answer, number):
    """Compares the user's answer and the correct one."""
    expected = expected_answer(number)

    if user_answer == expected:
        return True, correct_answer_message()
    return False, wrong_answer_message(user_answer, expected)


def expected_answer(number):
    """Return expected answer."""
    return 'yes' if number % 2 == 0 else 'no'


def wrong_answer_message(user_answer, correct_answer):
    """Return wrong answer message."""
    message = "'{answer}' is wrong answer ;(. Correct answer was '{correct}'"
    return message.format(answer=user_answer, correct=correct_answer)


def correct_answer_message():
    """Return correct answer message."""
    return 'Correct!'
