# -*- coding: utf-8 -*-

"""Brain calc game."""


from brain_games.game_engine import run
from brain_games.games import brain_calc


def main() -> None:
    """Run calc game."""
    run(brain_calc)


if __name__ == '__main__':
    main()
