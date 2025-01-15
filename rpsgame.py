import random
choices=['rock','paper','scissors']


def computer_selection():
    selection = random.choice(choices)
    return selection

def user_selection():
    while 1:
        user_choice = input("Choose rock, paper or scissors\n").strip().lower()
        if user_choice not in choices:
            print("Invalid choice! choose again.")
        else: 
            return user_choice
            
         
def game_logic(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" and computer_choice =="rock" or user_choice =="scissors" and computer_choice == "paper":
        return "user"
    else:
        return "computer"

def display_result(user_choice,computer_choice,winner,user_score,computer_score):
    print(f"You chose: {user_choice}, Computer chose: {computer_choice}")
    if winner=="Tie":
        print("Its a tie!")    
    elif winner== "user":
        print("Bravo! You Win this round.")
    else:
        print("Oops! You Lost this round")
    print(f"Your score: {user_score}, Computer Score: {computer_score}")

def game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = user_selection()
        computer_choice = computer_selection()
        result = game_logic(user_choice, computer_choice)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        display_result(user_choice, computer_choice, result, user_score, computer_score)

        selection = input("Do you want to continue? yes/no\n").strip().lower()
        if selection != "yes":
            break
    print("Game Over! You win the game" if user_score > computer_score else "Game tied" if user_score == computer_score else "Game Over! You lost the game")
 
if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    game()
    

    



