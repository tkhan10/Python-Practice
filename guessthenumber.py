import random;

def guess(x):
    print(f'Guess the number between 1 and {x}');
    random_number = random.randint(1,x);
    guess = 0

    while guess!= random_number:
        guess = int(input(f'Enter your number here:'))
        if guess>random_number:
            print('Sorry, Try again!, Too high')
        elif guess<random_number:
            print('Sorry, Try Again!. Too low')
        
    print(f'Wow Congratulation!- You have guessed the correct number {guess}')


guess(10)