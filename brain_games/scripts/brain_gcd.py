import random
import prompt


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    
    count = 0
    while count < 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        
        print(f'Question: {a} {b}')
        answer = input('Your answer: ')
        result = gcd(a, b)
        
        if int(answer) == result:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
        
        if count == 3:
            print(f'Congratulations, {name}!')
            return
    
    
if __name__ == "__main__":
    main()