import random

print('I picked a random number between 1 and 100.')
print('You have 7 tries left!')
print('Guess it!')

left = 1
right = 100

counter = 0
total_tries = 10

while counter < total_tries:
    print('Tries left: ' + str(total_tries - counter))
    print('######', left, right)
    player = int(input('Enter your number: '))
    counter = counter + 1
    if player < left:
        print('Your number is too small!')
    elif player > right:
        print('Your number is too big!')
    else:
        # We are inside the interval!
        if left == right:
            print('Hurray!')
            break
        if player - left < right - player:
            print('Your number is too small!')
            left = player + 1
        else:
            print('Your number is too big!')
            right = player - 1
        

if left != right or player != left:
    print('Game over! You are a bad player! Boooo!')
    pc = random.randint(left, right)
    print('The correct number was ' + str(pc) + '.')
else: print('Game over! You are a bad player! Boooo!')


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