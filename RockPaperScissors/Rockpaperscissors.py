import random

valid_choices=('r','p','s')
emoji={'r':'🪨','p':'🧾','s':'✂️'}
while True:
    user_choice=input("Rock Paper or Scissors(r/p/s):").lower()
    if user_choice not in valid_choices:
        print("Invalid Choice")
        continue

    computer_choice=random.choice(valid_choices)
    print(f"You chose:{emoji[user_choice]}")
    print(f"Computer chose:{emoji[computer_choice]}")

    if user_choice==computer_choice:
        print("TIE!")

    elif(
        (user_choice=='p' and computer_choice=='r') or
        (user_choice=='r' and computer_choice=='s') or
        (user_choice=='p' and computer_choice=='s')):
        print("You win")

    else:
        print("Computer wins")

    choose_continue=input("Do you want to continue(y/n):").lower()
    if choose_continue=='n':
        break

print("Thanks for playing")

        


