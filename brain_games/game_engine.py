# -*- coding: utf-8 -*-

"""Game engine functions."""


from random import randint
import sys
from brain_games.cli import get_user_answer, get_user_name


NUMBER_OF_ROUNDS = 3


def generate_number():
    """Return random number from range."""
    return randint(1, 10)


def check_answer(user_answer, correct_answer):
    """Check users answer."""

    if user_answer == correct_answer:
        message = 'Correct!'
        return True, message

    message = f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
    return False, message


def welcome_user(game=None):
    """Welcome user and print game"""
    print('Welcome to the Brain Games!')

    if game is None:
        print('')
    else:
        print(game)

    user_name = get_user_name()
    greeting = f'Hello, {user_name}!'

    if game is None:
        print(greeting)
    else:
        print(greeting)

    return user_name


def game_engine(game, question_and_answer=None):
    """Game engine."""
    user_name = welcome_user(game)

    if question_and_answer is None:
        sys.exit()

    correct_answers = 0

    while correct_answers < NUMBER_OF_ROUNDS:
        question, correct_answer = question_and_answer()
        print(question)

        res, message = check_answer(get_user_answer(), correct_answer)

        if res:
            print(message)
            correct_answers += 1
        else:
            print(message)
            print(f"Let's try again, {user_name}!")
            sys.exit()

    print(f'Congratulations, {user_name}!')
