#I can now roll dice with any number of sides any amount of times

import random

dice1 = int(input('Enter the sides of the dice: '))
num_roll = int(input('Enter how many of that dice you want to roll: '))

while num_roll > 0:

    roll = random.randint(1,dice1)
    print('Roll ' + str(num_roll) + ' is ' + str(roll))
    num_roll = num_roll - 1
