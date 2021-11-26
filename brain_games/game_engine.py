# -*- coding: utf-8 -*-

"""Game engine functions."""


from random import randint
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

    message = f"'{user_answer}' is wrong answer ;(. " \
              f"Correct answer was '{correct_answer}'."
    return False, message


def welcome_user():
    """Ask user name and print greeting."""
    user_name = get_user_name()
    greeting = f'Hello, {user_name}!'
    print(greeting)
    return user_name


def run(game=None):
    """Start game."""

    print('Welcome to the Brain Games!')

    if game:
        print(game.DESCRIPTION)

    print()
    user_name = welcome_user()

    if game:
        print()
        game_engine(user_name, game.make_question)


def game_engine(user_name, game):
    """Game engine."""

    correct_answers = 0

    while correct_answers < NUMBER_OF_ROUNDS:
        question, correct_answer = game()

        print(question)
        res, message = check_answer(get_user_answer(), correct_answer)
        print(message)

        if not res:
            print(f"Let's try again, {user_name}!")
            return
        else:
            correct_answers += 1
    else:
        print(f'Congratulations, {user_name}!')
