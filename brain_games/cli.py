# -*- coding: utf-8 -*-

"""CLI functions."""


import prompt


def get_user_name() -> str:
    """Prompt user for your name."""
    return prompt.string('May I have your name? ')


def get_user_answer() -> str:
    """Prompt user for answer."""
    return prompt.string('Your answer: ')
