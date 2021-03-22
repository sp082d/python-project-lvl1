import random
import prompt


def brain_even():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    k = 0

    while k < 3:
        number = random.randint(5, 30)
        parity = 'no' if number % 2 else 'yes'

        print('Question:', number)
        answer = prompt.string('Your answer: ')

        if answer == parity:
            print('Correct!')
            k += 1
        else:
            print(f"'{answer}' is wrong answer;(. Correct answer was '{parity}'.")
            print(f"Let's try again, {name}")
            break
    else:
        print(f'Congratulations, {name}!')


def main():
    brain_even()


if __name__ == '__main__':
    main()
