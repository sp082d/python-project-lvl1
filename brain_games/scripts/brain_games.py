#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Brain games welcome."""


from brain_games.game_engine import game_engine


def main():
    """Welcome user without running a game."""
    game_engine(None, None)


if __name__ == '__main__':
    main()
