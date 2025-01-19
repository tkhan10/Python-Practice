import random;
from words_list import words;

def is_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word :
        word = random.choice(words)

    print(word)
    return word;

is_valid_word(words)
