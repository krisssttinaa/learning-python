# simple guessing (number) game in python
import random

print('I picked a random number between 1 and 100.')
print('You have 7 tries left!')
print('Guess it!')

pc = random.randint(1, 100)

# print('*** Cheating! *** ' + str(pc))

player = -1
counter = 0
total_tries = 7

while player != pc and counter < total_tries:
    print('Tries left: ' + str(total_tries - counter))
    player = int(input('Enter your number: '))
    counter = counter + 1
    if player < pc:
        print('Your number is too small!')
    elif player > pc:
        print('Your number is too big!')

if pc == player:
    print('Hurray!')
else:
    print('Game over! You are a bad player! Boooo!')


##if condition_1:
##    print()
##elif condition_2:
##    print()
##elif condition_3:
##    print()
##elif condition_4:
##    print()
##else:
##    print()
##
##print('After the if!')
