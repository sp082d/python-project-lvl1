# -*- coding: utf-8 -*-

"""Brain even game."""

from brain_games.games.brain_even import make_question
from brain_games.scripts.brain_games import game_engine


QUESTION = 'Answer "yes" if number even otherwise answer "no".'


def main():
    """Run even game."""
    game_engine(QUESTION, make_question)


if __name__ == '__main__':
    main()
