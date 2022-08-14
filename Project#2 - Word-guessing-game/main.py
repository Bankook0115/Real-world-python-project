import random
name = str(input("What is your name ? : "))
print("Hello ", name , "Welcome to word guessing game")
print("You have 12 turn to guess the word. Good Luck!")
#word list
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
guess_target = random.choice(words)
print(guess_target)
max_turns = 12
turns = 0
guess = ""
while turns < max_turns:
    turns += 1
    new_guess = str(input(("Guess a character : ")))
    if new_guess not in guess_target:
        print("Wrong - Don't have", new_guess, "in the word")
    guess += new_guess
    # Show state of guessing
    wrong = 0
    for char in guess_target :
        if char in guess:
            print(char)
        else:
            print("_")
            wrong += 1
    # if all correct it will get wrong = 0 and show the answer       
    if wrong == 0:
        print("You win!")
        print("The word is : ", guess_target)
        break
    print("You remain ", max_turns-turns," turn to guess" )
if turns >= max_turns and wrong != 0 :
    print("You lose")

    





