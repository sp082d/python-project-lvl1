import random
import prompt


def brain_calc():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('What is the result of the expression?')

    operations = ['+', '-', '*']

    while True:
        f_number = str(random.randint(1, 10))
        s_number = str(random.randint(1, 10))
        rand_operation = random.choice(operations)

        expr = f_number + rand_operation + s_number
        val_expr = str(eval(expr))
        stack = (expr, val_expr)

        print('Question:', expr)
        answer = prompt.string('Your answer: ')
        print(stack)

        if answer == val_expr:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer;(. Correct answer was '{val_expr}'.")
            print(f"Let's try again, {name}!")
            break


def main():
    brain_calc()


if __name__ == '__main__':
    main()
