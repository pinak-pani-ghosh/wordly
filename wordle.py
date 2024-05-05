import random

f = open('five-letter-words.txt', 'r')
content = f.read()
f.close()
word_list = content.split()
word = random.choice(word_list)
print(word)
guess = input("Guess a word: ")
tries = 1
status = False
letters_left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_used = []
while tries < 6:
    if word == guess:
        status = True
        break
    else:
        idx = 0
        for letter in guess:
            if letter in letters_left:
                letters_left.remove(letter)
            if letter not in letters_used:
                letters_used.append(letter)
                letters_used.sort()
            if letter in word and letter == word[idx]:
                print(f"[{letter}]", end=' ')
            elif letter in word:
                print(f"({letter})", end=' ')
            else:
                print(f"__ ", end=' ')
            idx = idx + 1
    tries = tries + 1
    print(f'letters used = {letters_used}')
    print(f'letters left = {letters_left}')
    guess = input("Guess a word: ")
if status:
    print("you win!!")
else:
    print("you lose!!")
