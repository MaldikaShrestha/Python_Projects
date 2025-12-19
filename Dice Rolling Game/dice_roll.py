import random

print("This is a Dice rolling game.")
while True:
    user_choice=input("Do you wanna roll the dice(Y for yesand N for No)?")
    if user_choice=='y' or user_choice=='Y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"{die1},{die2}")

    elif user_choice=='N' or user_choice=='n':
        print("Thanks for playing.")
        break

    else:
        print("Invalid choice.")