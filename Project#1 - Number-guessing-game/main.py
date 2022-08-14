import random
import math

#user enter the range of number
Num_max = int(input("Key upper bound number : "))
Num_min = int(input("Key lower bound number : "))
#generate random number from user range
guess_target = random.randint(Num_min,Num_max)
# let user guess the number
count_guess = 0
max_guess = int(math.log2(Num_max - Num_min + 1))
print("You've only ", max_guess , " chances to guess the integer")
while count_guess < max_guess:
    count_guess += 1
    ans = int(input("Guess the Number : "))
    if (ans > guess_target):
        print("You guessed too high!")
    elif (ans < guess_target):
        print("You guessed too small!")
    elif (ans == guess_target):
        print("Congratulations!", " The number is " , ans, "With the guess in ", count_guess , "try")
        break

if (count_guess >= max_guess and ans != guess_target):
    print("The number is ", guess_target)
    print("Better Luck Next Time!")
    