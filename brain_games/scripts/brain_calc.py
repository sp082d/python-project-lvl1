import random
import prompt

def brain_calc():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('What is the result of the expression?')

    while True:
        number = random.randint(1, 10)
        operations = ['+', '-', '*']
        rand_operation = random.choice(operations)

        print(rand_operation)



def main():

    brain_calc()


if __name__ == '__main__':
    main()