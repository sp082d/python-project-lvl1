# -*- coding: utf-8 -*-

"""Brain progression game."""


from brain_games.game_engine import run
from brain_games.games import brain_progression


def main() -> None:
    """Run progression game."""
    run(brain_progression)


if __name__ == '__main__':
    main()
