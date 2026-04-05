import random
import prompt


def arifmetic():
    start = random.randint(1, 20)
    step = random.randint(2, 9)
    rand = random.randint(1, 10)
    nums = [start + i * step for i in range(10)]

    result_lst = ' '.join([str(i) for i in nums[:rand-1]]) + ' .. ' + ' '.join([str(i) for i in nums[rand:]])
    
    return result_lst, int(nums[rand-1])

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    
    count = 0
    while count < 3:
        a = random.randint(1, 100)
        nums = arifmetic()
        
        print(f'Question: {nums[0]}')
        answer = input('Your answer: ')
        
        if int(answer) == nums[1]:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{nums[1]}'.")
            print(f"Let's try again, {name}!")
            return
        
        if count == 3:
            print(f'Congratulations, {name}!')
            return
    
    
if __name__ == "__main__":
    main()