#create game Rock Scissor Paper game
import random
#Convert answer from int to rock scissor paper
def convert_choice(ans):
    if ans == 1:
        return "Rock"
    elif ans == 2:
        return "Scissor"
    elif ans == 3:
        return "Paper"

#create the winning condition
def check_ans(user,comp):
    result = ""
    if (user == 1 and comp == 2) or (user == 2 and comp == 1 ):
        result = "Rock"
    elif (user == 2 and comp == 3) or (user == 3 and comp == 2 ):
        result = "Scissor"
    elif(user == 1 and comp == 3) or (user == 3 and comp == 1 ):
        result = "Paper"
    return result
'''
Winning Rules as follows :

Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.
'''
# Inform the winning rule
print("Welcome to Rock Scissor Paper game\n")
print("Winning Rules as follows :", "\nRock vs Paper-> Paper wins","\nRock vs Scissor-> Rock wins","\nPaper vs Scissor-> Scissor wins.\n")
print("Here is your choice")
while True:
    print("Enter the choice :","\n1. Rock", "\n2. Scissor", "\n3. Paper")
    #Receive user choice
    user_choice = int(input("User choice : "))
    #Check the answer of user
    while user_choice < 1 or user_choice > 3:
        print("Please enter the choice only 1,2 or 3")
        user_choice = int(input("User choice : "))
    #Finish function convert
    #Random comp choice
    comp_choice = random.randint(1,3)
    #Computer choice will not equal with user choice
    while comp_choice == user_choice:
        comp_choice = random.randint(1,3)
    print("\nNow It's computer turn...")
    print("\nComputer choice is : ", convert_choice(comp_choice))
    #Show versus display
    print(convert_choice(user_choice) , "VS" , convert_choice(comp_choice))


    #Show the result & winner
    result = check_ans(user_choice,comp_choice)
    #Check the winner
    if convert_choice(user_choice) == result:
        winner = "User Wins"
    else:
        winner = "Computer Wins"

    print(result,"wins =>" , winner)

    print("\nDo you want to play again : Yes/No")
    newgame = str(input("Y / N : "))
    if newgame == "N" or newgame == "n":
        break

print("\nThanks you for playing the game")

