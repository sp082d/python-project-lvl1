# -*- coding: utf-8 -*-

"""Brain progression game."""


from brain_games.games.brain_progression import make_question
from brain_games.game_engine import game_engine


QUESTION = 'What number is missing in the progression?'


def main():
    """Run progression game."""
    game_engine(QUESTION, make_question)


if __name__ == '__main__':
    main()
