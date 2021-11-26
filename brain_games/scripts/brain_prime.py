# -*- coding: utf-8 -*-

"""Brain prime game."""


from brain_games.game_engine import run
from brain_games.games import brain_prime


def main() -> None:
    """Run prime game."""
    run(brain_prime)


if __name__ == '__main__':
    main()
