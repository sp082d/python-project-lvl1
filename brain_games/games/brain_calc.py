# -*- coding: utf-8 -*-

"""Brain calc game functions."""


from random import choice

from brain_games.games.common import generate_number


def sum_numbers(num1, num2):
    """Sum of two numbers."""
    return num1 + num2


def subtract_numbers(num1, num2):
    """Subtracts the second from the first number."""
    return num1 - num2


def multiply_numbers(num1, num2):
    """Multiply two numbers."""
    return num1 * num2


operations = {
    '+': sum_numbers,
    '-': subtract_numbers,
    '*': multiply_numbers,
}


def generate_operation():
    """Generate random operation."""
    return choice(list(operations.keys()))


def correct_answer(num1, operation, num2):
    """Return correct answer."""
    return str(operations[operation](num1, num2))


def make_question():
    """Generate game question."""
    num1 = generate_number()
    num2 = generate_number()
    operation = generate_operation()

    question = 'Question: {first_number} {operation} {second_number}'.\
        format(first_number=num1, operation=operation, second_number=num2)

    answer = correct_answer(num1, operation, num2)
    return question, answer

