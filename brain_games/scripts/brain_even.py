import random
import prompt

print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')

print('Answer "yes" if the number is even, otherwise answer "no".')

k = 0

while k < 3:
    number = random.randint(5, 30)
    parity = 'no' if number % 2 else 'yes'
    stack = (number, parity)

    print('Question: ', number)
    answer = prompt.string('Your answer: ')
    print(stack)

    if answer == parity:
        print('Correct!')
        k += 1
    else:
        print(f"Let's try again, {name}")
        break
else:
    print(f'Congratulations, {name}!')

