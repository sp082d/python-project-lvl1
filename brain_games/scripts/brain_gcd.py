# -*- coding: utf-8 -*-

"""Brain GCD game."""


from brain_games.games.brain_gcd import make_question
from brain_games.game_engine import game_engine


QUESTION = 'Find the GCD of given numbers.'


def main():
    """Run even game."""
    game_engine(QUESTION, make_question)


if __name__ == '__main__':
    main()
