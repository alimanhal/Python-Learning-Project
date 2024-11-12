import random

number_to_guess=random.randint(1, 100)
while True:
    try:
        guess = int(input('Guess the number between 1 and 100 : '))
        if  guess <=1 or guess >= 100:
            print('Enter a number between 1 and 100')
        elif guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!!')
        elif guess == number_to_guess:
            print(' Congratulations ! You are right')
            break

    except  ValueError:
        print('Enter a valid number')
    

