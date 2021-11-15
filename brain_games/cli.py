# -*- coding: utf-8 -*-

"""CLI functions."""

import prompt


def get_user_name():
    """Prompt user for his/her name."""
    user_name = prompt.string('May I have your name? ')
    return user_name


def get_user_answer():
    """Prompt user for answer."""
    answer = prompt.string('Your answer: ')
    return answer
