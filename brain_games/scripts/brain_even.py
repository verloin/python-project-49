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

        if (n % 2 == 0 and answer == 'yes') or (n % 2 != 0 and answer == 'no'):
            count += 1
            print('Correct!')
        else:
            if answer == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
            return
        
        if count == 3:
            print(f'Congratulations, {name}!')
            return
    
    
if __name__ == "__main__":
    main()