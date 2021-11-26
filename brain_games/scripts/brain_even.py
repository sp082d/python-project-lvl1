# -*- coding: utf-8 -*-

"""Brain even game."""


from brain_games.game_engine import run
from brain_games.games import brain_even


def main() -> None:
    """Run even game."""
    run(brain_even)


if __name__ == '__main__':
    main()
