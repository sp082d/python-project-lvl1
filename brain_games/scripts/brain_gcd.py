import random
import prompt
import math


def brain_gcd():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Find the greatest common divisor of given numbers.')

    while True:
        f_number = random.randint(1, 10)
        s_number = random.randint(1, 10)
        gcd = str(math.gcd(f_number, s_number))

        print('Question: ', f_number, s_number)
        answer = prompt.string('Your answer: ')

        if answer == gcd:
            print('Correct!')
        else:
            print(f" '{answer}' is wrong answer;(. Correct answer was '{gcd}'.")
            print(f"Let's try again, {name}!")
            break


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
