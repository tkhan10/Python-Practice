import random

def guess_computer(x):
    low = 1
    high = x 
    userInput = ''
    while userInput != 'c':
        random_number = random.randint(low, high)
        userInput = input(f'Add your input for {random_number} is low(L), high (H) or correct (C)').lower()
        if userInput == 'h':
            high = random_number-1
        elif userInput == 'l':
            low = random_number+1
    
    print(f'Wow - Congratulation computer guessed the number {random_number}!')

guess_computer(1000)