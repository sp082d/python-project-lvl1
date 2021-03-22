import random
import prompt
import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    else:
        return True


def brain_prime():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while True:
        num = random.randint(1, 20)
        num_prime = 'yes' if is_prime(num) else 'no'

        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')

        if answer == num_prime:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer;(. Correct answer was '{num_prime}'.")
            print(f"Let's try again, {name}!")
            break


def main():
    brain_prime()


if __name__ == '__main__':
    main()
