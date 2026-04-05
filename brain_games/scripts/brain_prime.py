import random
import prompt


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime.')
    
    count = 0
    while count < 3:
        n = random.randint(1, 1000)
        
        print(f'Question: {n}')
        answer = input('Your answer: ')
        result = True if answer == 'yes' else False
        
        if result == is_prime(n):
            count += 1
            print('Correct!')
        else:
            print(f"'{result}' is wrong answer ;(. Correct answer was '{is_prime(n)}'.")
            print(f"Let's try again, {name}!")
            return
        
        if count == 3:
            print(f'Congratulations, {name}!')
            return
    
    
if __name__ == "__main__":
    main()