# -*- coding: utf-8 -*-

"""Brain even game functions."""

from typing import Tuple
from brain_games.game_engine import generate_number


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_question() -> Tuple[str, str]:
    """Generate game question."""
    number = generate_number()
    question = f'Question: {number}'
    answer = correct_answer(number)
    return question, answer


def correct_answer(number: int) -> str:
    """Return expected answer."""
    return 'yes' if number % 2 == 0 else 'no'
