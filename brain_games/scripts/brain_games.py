#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Program entry point."""


import sys
from brain_games.cli import get_user_answer, get_user_name
from brain_games.games.common import check_answer


NUMBER_OF_ROUNDS = 3


def game_engine(game_task, question_and_answer):
    """Game engine."""
    user_name = welcome_user(game_task)
    correct_answers = 0

    while correct_answers < NUMBER_OF_ROUNDS:
        question, correct_answer = question_and_answer()
        print(question)
        result, message = check_answer(get_user_answer(), correct_answer)
        if result:
            print(message)
            correct_answers += 1
        else:
            print(message)
            print("Let's try again, {user_name}!".format(user_name=user_name))
            sys.exit()
    print('Congratulations, {user_name}!'.format(user_name=user_name))


def welcome_user(game_task):
    """Run game."""
    print('Welcome to the Brain Games!')
    print(game_task)

    user_name = get_user_name()
    greeting = 'Hello, {user_name}!'.format(user_name=user_name)
    print(greeting)
    return user_name


def main():
    """Welcome user without running a game."""
    print('Welcome to the Brain Games!')
    user_name = get_user_name()
    greeting = 'Hello, {user_name}!'.format(user_name=user_name)
    print(greeting)


if __name__ == '__main__':
    main()
