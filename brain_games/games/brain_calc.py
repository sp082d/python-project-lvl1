# -*- coding: utf-8 -*-

"""Brain calc game functions."""

import operator
from typing import Tuple
from random import choice
from brain_games.game_engine import generate_number


DESCRIPTION = 'What is the result of the expression?'


operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_operation() -> str:
    """Generate random operation."""
    return choice(list(operations.keys()))


def correct_answer(num1: int, operation: str, num2: int) -> str:
    """Return correct answer."""
    return str(operations[operation](num1, num2))


def make_question() -> Tuple[str, str]:
    """Generate game question."""
    num1 = generate_number()
    num2 = generate_number()
    operation = generate_operation()

    question = f'Question: {num1} {operation} {num2}'

    answer = correct_answer(num1, operation, num2)

    return question, answer
