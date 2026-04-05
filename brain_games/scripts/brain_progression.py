import random

import prompt


def arifmetic():
    start = random.randint(1, 20)
    step = random.randint(2, 9)
    hidden_index = random.randint(0, 9)  # индекс скрытого элемента
    nums = [start + i * step for i in range(10)]
    
    # Формируем строку с вопросом
    parts = []
    for i, num in enumerate(nums):
        if i == hidden_index:
            parts.append('..')
        else:
            parts.append(str(num))
    
    result_lst = ' '.join(parts)
    return result_lst, nums[hidden_index]


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    
    count = 0
    while count < 3:
        nums = arifmetic()
        
        print(f'Question: {nums[0]}')
        answer = input('Your answer: ')
        
        if int(answer) == nums[1]:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{nums[1]}'.")
            print(f"Let's try again, {name}!")
            return
        
        if count == 3:
            print(f'Congratulations, {name}!')
            return
    
    
if __name__ == "__main__":
    main()