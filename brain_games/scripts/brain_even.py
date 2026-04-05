import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        n = random.randint(1, 100)
        print(f'Question: {n}')
        answer = input('Your answer: ')
        
        is_even = n % 2 == 0
        correct_answer = 'yes' if is_even else 'no'
        
        if answer == correct_answer:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        if count == 3:
            print(f'Congratulations, {name}!')
            return
    
    
if __name__ == "__main__":
    main()