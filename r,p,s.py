import random
options = ["rock", "paper", "scissor"]
while True:
    user_ch = input("Enter rock, paper, or scissor: ")
    comp_ch = random.choice(options)
    print("You chose:", user_ch)
    print("Computer chose:", comp_ch)

    if user_ch == comp_ch:
        print("It's a tie")
    elif user_ch == "rock" and comp_ch == "scissor":
        print("You win!")
    elif user_ch == "paper" and comp_ch == "rock":
        print("You win!")
    elif user_ch == "scissor" and comp_ch == "paper":
        print("You win!")
        break
    else:
        print("Computer wins")
