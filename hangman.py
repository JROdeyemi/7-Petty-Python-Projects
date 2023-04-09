import random
import hangman_words

word_list = hangman_words.words

hidden_word = random.choice(word_list)
hidden_word = hidden_word.lower()


dashes = []

for letter in hidden_word:
    dashes.append('_')

print(f'Hidden word is {dashes}')


life = 6

guess_list = []

while '_' in dashes:
    player_guess = input('Guess a letter. ')
    player_guess = player_guess.lower()

    if player_guess in guess_list:
        print('You have previously guessed this word. Try again.')
    if player_guess not in guess_list:
        for i in range(0, len(hidden_word)):
            if hidden_word[i] == player_guess:
                dashes[i] = player_guess

    if player_guess not in hidden_word:
        if player_guess in guess_list:
            life = life
        if player_guess not in guess_list:
            life = life - 1
            print(
                f'You guessed a wrong letter. You have lost a life. You have {life} lives left.')
            if life == 0:
                print(
                    f'Game Over. Unfortunately, you could not guess the word {hidden_word}')
                break

    for g in player_guess:
        if g not in guess_list:
            guess_list.append(player_guess)

    print(dashes)
    if '_' not in dashes:
        print(
            f'Congratulations! You have found all the letter in the word {hidden_word}.')
