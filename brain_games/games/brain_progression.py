# -*- coding: utf-8 -*-

"""Brain progression game functions."""


from random import choice
from typing import Tuple, List
from brain_games.game_engine import generate_number


DESCRIPTION = 'What number is missing in the progression?'


DELTA = 10


def make_progression() -> List[str]:
    """Generate arithmetic progression."""
    start = generate_number()
    end = generate_number(start=start + DELTA // 2, end=start + DELTA)
    return list(map(str, range(start, end)))


def make_question() -> Tuple[str, str]:
    """Generate game question."""
    progression = make_progression()
    secret = choice(progression)
    progression = ' '.join(['..' if num == secret else
                            num for num in progression])
    return f'Question: {progression}', \
           secret
