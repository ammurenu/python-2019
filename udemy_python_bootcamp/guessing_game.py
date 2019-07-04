#The Challenge:

#Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

#If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#On a player's first turn, if their guess is within 10 of the number, return "WARM!"
#further than 10 away from the number, return "COLD!"
#On all subsequent turns, if a guess is closer to the number than the previous guess return "WARMER!"
#farther from the number than the previous guess, return "COLDER!"
#When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

from random import randint

number = randint(1,101)
print(number)
guess_list = [0]
while True:
    l = len(guess_list)
    guess_num = int(input('Guess the number: '))
    if guess_num == number:
        print(f'Congratulations! You have guessed the number in {l} guesses')
        break
    if guess_num < 1 or guess_num > 100:
        print('OUT OF BOUNDS!')
        continue
    if l == 1:
        if abs(guess_num - number) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        if abs(guess_num - number) < abs(guess_list[-1] - number):
            print('WARMER!')
        else:
            print('COLDER!')
    guess_list.append(guess_num)
    #print(guess_list)


    
        



