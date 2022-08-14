import random
print('Guess the word! HINT: word is a name of a fruit')
#word list
someWords = "apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon"
#pre processing data
words = someWords.split(" ")
# random word on the lists
print(words)
guess_word = random.choice(words)
print(guess_word)
#Show _ on form the word
for i in guess_word:
    print("_" , end = ' ')
max_turns = len(guess_word)+2
print("\nYou have" , max_turns , "chance to guess")
turns = 0
guess = ""
while turns < max_turns:
    turns += 1
    new_guess = str(input(("\nEnter the letter to guess : ")))
    if new_guess not in guess_word:
        print("Sorry! - Don't have", new_guess, "in the word")
    guess += new_guess
    # Show state of guessing
    wrong = 0
    for char in guess_word :
        if char in guess:
            print(char, end = " ")
        else:
            print("_", end = " ")
            wrong += 1
    # if all correct it will get wrong = 0 and show the answer       
    if wrong == 0:
        print("\nYou win!")
        print("The word is :", guess_word)
        break
    print("\nYou remain ", max_turns-turns," turn to guess" )
if turns >= max_turns and wrong != 0 :
    print("\nYou lose")
