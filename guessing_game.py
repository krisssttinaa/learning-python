#This line imports the random module, which allows you to generate random numbers.
import random

#These three lines print introductory messages to the console to inform the player about the game.
print('I picked a random number between 1 and 100.')
print('You have 7 tries left!')
print('Guess it!')

#This line generates a random integer between 1 and 100 (inclusive) and assigns it to the variable pc
pc = random.randint(1, 100)

#We can cheat, but we don't :)
#print('*** Cheating! ***' + str(pc))

#These lines initialize three variables
player = -1
counter = 0
total_tries = 7

#This line starts a while loop
while player != pc and counter < total_tries:
    print('Tries left: ' + str(total_tries - counter))
    #This line prompts the player to enter their guess and stores it as an integer in the player var
    player = int(input('Enter your number: '))
    counter = counter + 1
    if player < pc:
        print('Your number is too small!')
    elif player > pc:
        print('Your number is too big!')

"""after the while loop ends, this block checks if the player has 
guessed the correct number. If they have, it prints 'Hurray!' indicating 
success; otherwise, it prints 'Game over! ... indicating failure."""
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