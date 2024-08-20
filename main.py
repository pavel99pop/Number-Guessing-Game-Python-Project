import random

max_range = input('Insert range: ')

if max_range.isdigit():
    max_range = int(max_range)
    if max_range <= 0:
        print('Error! Range must be higher than 0!')
        quit()

else:
    print('Error! Range must be a number!')
    quit()

random_number = random.randint(0, max_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Error! Please guess a number!')
        continue

    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
        print('Too high!')
    else:
        print('Too low!')

print('You took ' + str(guesses) + ' guesses!')