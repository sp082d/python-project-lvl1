import random
import prompt


def brain_progression():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('What number is missing in the progression?')

    while True:
        start_seq = random.randint(1, 5)
        end_seq = random.randint(6, 13)
        seq = list(range(start_seq, end_seq))
        new_seq = seq.copy()

        rand_pos = random.randint(0, len(seq) - 1)
        elem = str(seq[rand_pos])
        new_seq[rand_pos] = ".."

        print(f'Question: {new_seq}')
        answer = prompt.string('Your answer: ')

        if elem == answer:
            print('Correct!')
        else:
            print(f" '{answer}' is wrong answer;(. Correct answer was '{seq[rand_pos]}'.")
            print(f"Let's try again, {name}!")
            break


def main():
    brain_progression()


if __name__ == '__main__':
    main()




