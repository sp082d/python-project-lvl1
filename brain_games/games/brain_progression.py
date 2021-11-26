# -*- coding: utf-8 -*-

"""Brain progression game functions."""


from random import choice, randint
from typing import Tuple, List

START_UPPER = 10

DESCRIPTION = 'What number is missing in the progression?'


def make_progression() -> List[str]:
    """Generate arithmetic progression."""
    start = randint(1, START_UPPER)
    end = randint(start + START_UPPER // 2, start + START_UPPER)

    return list(map(str, range(start, end)))


def make_question() -> Tuple[str, str]:
    """Generate game question."""
    progression = make_progression()
    secret = choice(progression)

    progression = ' '.join(['..' if num == secret else
                            num for num in progression])

    return f'Question: {progression}', secret
