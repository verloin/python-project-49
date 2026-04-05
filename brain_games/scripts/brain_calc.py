import random

import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        options = ['-', '+', '*']
        op = random.choice(options)
        
        result = eval(f"{a} {op} {b}")
        
        print(f'Question: {a} {op} {b}')
        answer = input('Your answer: ')

        if int(answer) == result:
            count += 1
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{result}'."
            )
            print(f"Let's try again, {name}!")
            return
        
        if count == 3:
            print(f'Congratulations, {name}!')
            return
    
    
if __name__ == "__main__":
    main()