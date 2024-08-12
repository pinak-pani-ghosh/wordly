import random


f = open('five-letter-words.txt', 'r')  # get words
content = f.read()
f.close()
word_list = content.split()  # split the words
word = random.choice(word_list)  # choose a random word from list
print(word)
tries = 1  # no of tries
status = False  # win status
letters_left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_used = []
while tries <= 5:  # tries till limit
    print(f'try: {tries}')
    guess = input("Guess a word: ")  # guess word

    try:
        if not guess.isalpha() or len(guess) != 5:
            raise ValueError("Warning: Word should contain only alphabets and 5 letters long.")
    except ValueError as e:
        print(e)
    else:
        print("Word is valid.")

        if word == guess:
            status = True  # if win status change
            break
        else:
            i = 0
            while i < 5:

                if guess[i] in word:
                    if guess[i] == word[i]:
                        print(f"[{guess[i]}]", end=' ')  # color the letter green
                    else:
                        print(f"({guess[i]})", end=' ')  # color the letter yellow
                else:
                    print(f"__ ", end=' ')  # leave it empty

                if guess[i] in letters_left:
                    letters_left.remove(guess[i])  # remove letters if used
                if guess[i] not in letters_used:
                    letters_used.append(guess[i])  # add letters if used
                    letters_used.sort()

                i = i + 1

        print(f'\nletters used = {letters_used}')  # letters used
        print(f'letters left = {letters_left}')  # letters not used

        tries = tries + 1

if status:
    print("you win!!")
else:
    print("you lose!!")
