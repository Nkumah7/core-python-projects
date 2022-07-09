import sys
import random
from pyfiglet import Figlet

fig = Figlet()
fig.setFont(font="small")

def main():    
    print(fig.renderText("Rock-Paper-Scissors")) 
    
    while True:              
        user_choice = get_user_answer() 
        computer_choice = get_computer_choice()  
        result = get_result(user_choice, computer_choice)
        print(f"{result}\n")
        print("Would you like to play again? ")
        
def get_user_answer():
    initiate_game = ["yes", "y"]
    end_game = ["no", "n"]
    
    while True:
        try:
            answer = input("Type yes/y to play or no/n to not play: ").lower().strip()
            if answer in initiate_game:
                print("Great! Let's Begin\n") 
                return True
            elif answer in end_game:                   
                sys.exit(fig.renderText("Game Over"))  
            print("\nPlease input a valid answer")         
        except ValueError:            
            pass           
   
def get_user_choice():
    choice_list = ["rock", "paper", "scissors"]
    while True:
        try:
            user_choice = input("Rock, Paper or Scissors: ").lower().strip()
            if user_choice in choice_list:
                return user_choice.title()
            print("\nPlease make a choice")
        except ValueError:
            pass
        
def get_computer_choice():
    computer_choice  = ["rock", "paper", "scissors"]
    
    if random.choice(computer_choice) == "rock":
        return "rock".title()
    elif random.choice(computer_choice) == "paper":
        return "paper".title()
    else:
        return "scissors".title()
    
def get_result(user_choice, computer_choice):
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYour choice:       {user_choice}")
    print(f"Computer choice:   {computer_choice}")
    
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if user_choice == "rock".title() and computer_choice == "scissors".title():
        return "You win!"
    elif user_choice == "paper".title() and computer_choice == "rock".title():
        return "You win!"
    elif user_choice == "scissors".title() and computer_choice == "paper".title():
        return "You win!"
    else:
        return "You lose!"

if __name__ == "__main__":
    main()    