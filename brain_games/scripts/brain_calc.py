# -*- coding: utf-8 -*-

"""Brain calc game."""


from brain_games.games.brain_calc import make_question
from brain_games.scripts.brain_games import game_engine


QUESTION = 'What is the result of the expression?'


def main():
    """Run calc game."""
    game_engine(QUESTION, make_question)


if __name__ == '__main__':
    main()
