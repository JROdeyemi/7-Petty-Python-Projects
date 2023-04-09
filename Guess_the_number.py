import random


target = random.randrange(1, 51)
tries = 4

while tries != 0:

    player_guess = int(input('Guess a number between 1 - 50. '))

    if target > player_guess:
        diff = target - player_guess
        tries = tries - 1
        if diff >= 10:
            print(
                f'The number is well bigger than that. You have {tries} tries left.')
        else:
            print(
                f'Incorrect, but you are close. You have {tries} tries left.')

    if target < player_guess:
        diff = player_guess - target
        tries = tries - 1
        if diff >= 10:
            print(
                f'The number is way below that. You have {tries} tries left.')
        else:
            print(
                f'Incorrect, but you are close. You have {tries} tries left.')

    if tries == 0:
        print(f'Unfortunately, you could not guess the number {target}')

    if target == player_guess:
        print('BRILLIANT! You correctly guessed the number!')
        break
