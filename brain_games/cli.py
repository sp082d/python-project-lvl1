# -*- coding: utf-8 -*-

"""CLI functions."""

import prompt


def welcome_user():
    """Requests a username and returns a greeting."""
    username = prompt.string('May I have your name? ')
    greeting = 'Hello, {}!'.format(username)
    return greeting
