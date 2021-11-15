# -*- coding: utf-8 -*-

"""Brain even game."""

import prompt
from brain_games.brain_even import check_answer, generate_number
from brain_games.cli import welcome_user

NUMBER_OF_ROUNDS = 3


def game(user_name):
    """Game main logic."""
    correct_answers = 0
    while correct_answers < NUMBER_OF_ROUNDS:
        number = generate_number()
        print('Question: {}'.format(number))
        user_answer = prompt.string('Your answer: ')
        is_right, message = check_answer(user_answer, number)
        print(message)

        if not is_right:
            print("Let's try again, {}!".format(user_name))
            break

        correct_answers += 1

        print('Congratulations, {}!'.format(user_name))


def main():
    """Run game."""
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    greeting = welcome_user()
    print(greeting)
    user_name = greeting.split(',')[1].strip()[:-1]
    game(user_name)


if __name__ == '__main__':
    main()
