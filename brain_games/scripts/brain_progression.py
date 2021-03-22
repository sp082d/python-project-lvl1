import random
import prompt


def brain_progression():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('What number is missing in the progression?')

    # while True:
    start_seq = random.randint(1, 10)
    end_seq = random.randint(11, 20)

    seq = range(start_seq, end_seq)

    print(seq)


def main():
    brain_progression()


if __name__ == '__main__':
    main()




