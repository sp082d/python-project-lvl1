# -*- coding: utf-8 -*-

"""Brain GCD game."""


from brain_games.game_engine import run
from brain_games.games import brain_gcd


def main() -> None:
    """Run even game."""
    run(brain_gcd)


if __name__ == '__main__':
    main()
