

variable_options=["rock", "paper", "scissors"]

from random import choice

def winner(user_choice, computer_choice):

    if user_choice == "rock" and computer_choice == "rock":
        #print("It's a tie!")
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "paper":
        #print("The computer wins")
        return "The computer wins"
    elif user_choice == "rock" and computer_choice == "scissors":
        #print("The user wins")
        return "The user wins"

    elif user_choice == "paper" and computer_choice == "rock":
        #print("The computer wins") #there is a bug
        return "The user wins"
    elif user_choice == "paper" and computer_choice == "paper":
        #print("It's a tie!")
        return "It's a tie!"
    elif user_choice == "paper" and computer_choice == "scissors":
        #print("The user wins") #there is a bug
        return "The computer wins"

    elif user_choice == "scissors" and computer_choice == "rock":
        #print("The computer wins")
        return "The computer wins"
    elif user_choice == "scissors" and computer_choice == "paper":
        #print("The user wins")
        return "The user wins"
    elif user_choice == "scissors" and computer_choice == "scissors":
        #print("It's a tie!")
        return "It's a tie!"
    return "OOPS - TODO"


if __name__ == "__main__":

    # ONLY RUN THE CODE IF RUN THE CODE FROM THE COMMAND LINE
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in variable_options:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(variable_options)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #
    print(winner(u,c))
    #if u == "rock" and c == "rock":
    #    print("It's a tie!")
    #elif u == "rock" and c == "paper":
    #    print("The computer wins")
    #elif u == "rock" and c == "scissors":
    #    print("The user wins")
    #
    #elif u == "paper" and c == "rock":
    #    print("The computer wins")
    #elif u == "paper" and c == "paper":
    #    print("It's a tie!")
    #elif u == "paper" and c == "scissors":
    #    print("The user wins")
    #
    #elif u == "scissors" and c == "rock":
    #    print("The computer wins")
    #elif u == "scissors" and c == "paper":
    #    print("The user wins")
    #elif u == "scissors" and c == "scissors":
    #    print("It's a tie!")
