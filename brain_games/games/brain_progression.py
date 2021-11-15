# -*- coding: utf-8 -*-

"""Brain progression game functions."""


from random import choice, randint


def make_progression():
    """Generate arithmetic progression."""
    start = randint(1, 10)
    end = randint(start + 5, start + 10)

    return list(map(str, range(start, end)))


def make_question():
    """Generate game question."""
    progression = make_progression()
    secret = choice(progression)

    progression = ' '.join(['..' if num == secret else
                            num for num in progression])
    question = 'Question: {progression}'.format(progression=progression)
    return question, secret