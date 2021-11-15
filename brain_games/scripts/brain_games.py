#!/usr/bin/env python
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    greeting = welcome_user()
    print(greeting)


if __name__ == "__main__":
    main()
