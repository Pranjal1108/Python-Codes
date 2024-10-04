import random
choices = ["rock","paper","scissor"]
print(choices)


while True:
    user_choice = str(input("We're playing Rock Paper Scissors, Pick your Choice : "))

    AI_pick = random.choice(choices)    

    if user_choice not in choices:
        print("Error: check either the spellings or the choice is in the choices")
    else:
        if AI_pick == user_choice:
            print("Draw")
        elif AI_pick == "paper" and user_choice == "scissor":
            print("You Win")
        elif AI_pick == "rock" and user_choice == "paper":
            print("You Win")
        elif AI_pick == "scissor" and user_choice == "rock":
            print("You Win")
        else:
            print("You Lose")

    print(f"The AI picked:{AI_pick}")

    Continuation = input("Do You Want to continue? (yes/no): ")
    if Continuation == "yes":
        continue
    else:
        break

    