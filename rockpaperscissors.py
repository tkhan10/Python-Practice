import random;

def play():
    user = input("Enter you choice('r' for Rock, 'p' for paper and 's' for scissors)")
    computer = random.choice(['r', 's', 'p']);
    #  r>s, s>p and p>r
    if user == computer:
        print("Your match has been tie");
        return;
    
    if is_win(user, computer):
        print("You won!")
        return;


    print("You Lost!")

def is_win(user, computer):
    if (user=='r' and computer == 's') or (user=='s' and computer == 'p') or (user=='p' and computer == 's'):
        return True;

play()