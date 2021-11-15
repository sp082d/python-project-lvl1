import prompt


def welcome_user():
    username = prompt.string('May I have your name? ')
    greeting = 'Hello, {}!'.format(username)
    print(greeting)
