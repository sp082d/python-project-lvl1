# -*- coding: utf-8 -*-

"""Game engine functions."""


from random import randint
from typing import Tuple, Union, Callable
from brain_games.cli import get_user_answer, get_user_name


NUMBER_OF_ROUNDS = 3


def generate_number() -> int:
    """Return random number from range."""
    return randint(1, 10)


def check_answer(user_answer: str, correct_answer: str) -> Tuple[bool, str]:
    """Check users answer."""

    if user_answer != correct_answer:
        return False, f"'{user_answer}' is wrong answer ;(." \
                      f" "f"Correct answer was '{correct_answer}'."
    else:
        return True, 'Correct!'


def welcome_user() -> str:
    """Ask user name and print greeting."""
    user_name = get_user_name()
    greeting = f'Hello, {user_name}!'
    print(greeting)

    return user_name


def run(game=None) -> None:
    """Start game."""
    print('Welcome to the Brain Games!')

    if game:
        print(game.DESCRIPTION)
        print()
        game_engine(welcome_user(), game.make_question)
    else:
        print()
        welcome_user()


def game_engine(user_name: str,
                game: Union[None, Callable[[], Tuple[str, str]]]) -> None:
    """Game engine."""

    correct_answers = 0

    while correct_answers < NUMBER_OF_ROUNDS:
        question, correct_answer = game()

        print(question)
        res, message = check_answer(get_user_answer(), correct_answer)
        print(message)

        if res:
            correct_answers += 1
        else:
            print(f"Let's try again, {user_name}!")
            return
    else:
        print(f'Congratulations, {user_name}!')
