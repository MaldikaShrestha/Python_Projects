import random

actual_number=random.randint(1,100)
while True:
    try:
        guess=int(input(("Guess the number between 1 and 100:")))
        if guess==actual_number:
            print("Congratulations you have successfully guessed the number!!")
            break

        elif guess < actual_number:
            print("Low")

        elif guess > actual_number:
            print("High")

        else:
            print("Invalid Choice. Enter the number.")

    except:
        print("please enter a valid number:")
