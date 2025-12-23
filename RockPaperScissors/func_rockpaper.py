import random

valid_choices=('r','p','s')
emoji={'r':'🪨','p':'🧾','s':'✂️'}

def get_user_choice():
    while True:
        user_choice=input("Rock paper or scissors(r/p/s):").lower()
        if user_choice in valid_choices:
            return user_choice
        else:
            print("Invalid choice.")

def display_choice():
    print(f"You chose {emoji[user_choice]}")
    print(f"Computer chose {emoji[computer_choice]}")

def decide_winner():
    if user_choice==computer_choice:
        print("Its a tie!!")
    elif(
        (user_choice=='r' and computer_choice=='s') or
        (user_choice=='p' and computer_choice=='r') or
        (user_choice=='s' and computer_choice=='p')
    ):
        print("You win!")
    else:
        print("Computer wins")



while True:
    user_choice=get_user_choice()
    computer_choice=random.choice(valid_choices)
    display_choice()
    decide_winner()
    replay_choice=input("Do you want to play again(y/n)?").lower()
    if replay_choice=='n':
        break

print("Thank you for playing!!!")
