import random
def start():
    print("Welcome to Black Jack Game")
    a = input("Do you want to start the game? (y/n ) ")
    if a == 'y':
        user_1 = random.randint(1, 10)
        user_2 = random.randint(1, 10)
        print(f"Your cards are: {user_1, user_2}")
        user_total = user_1 + user_2
        if user_total == 20:
            print("Black Jack! You won")

        computer_1 = random.randint(1, 10)
        computer_2 = random.randint(1, 10)
        print(f"Computer's card is: {computer_1}")
        computer_total = computer_1 + computer_2

        b = input("Do you want another card? (y/n) ")
        if b == 'y':
            user_3 = random.randint(1, 10)
            print(f"Now your cards are: {user_1, user_2, user_3}")
            user_total += user_3
            print(f"Computer's cards are: {computer_1, computer_2}")
            if user_total <= 21 and user_total > computer_total:
                print("Congrats! You won")
                c = input("Want to play again? (y/n) ")
                if c == 'y':
                    start()
                else:
                    print("Good Bye")
            elif user_total == computer_total:
                print("Its a draw")
                c = input("Want to play again? (y/n) ")
                if c == 'y':
                    start()
                else:
                    print("Good Bye")
            else:
                print("You lost")
                c = input("Want to play again? (y/n) ")
                if c == 'y':
                    start()
                else:
                    print("Good Bye")
        else:
            print(f"Computer's cards are: {computer_1, computer_2}")
            if user_total > computer_total:
                print("Congrats! You won")
                c = input("Want to play again? (y/n) ")
                if c == 'y':
                    start()
                else:
                    print("Good Bye")
            elif user_total == computer_total:
                print("Its a draw")
                c = input("Want to play again? (y/n) ")
                if c == 'y':
                    start()
                else:
                    print("Good Bye")
            else:
                print("You lost")
                c = input("Want to play again? (y/n) ")
                if c == 'y':
                    start()
                else:
                    print("Good Bye")
    else:
        print("Aya hee kion tha?")
        c = input("Want to play again? (y/n) ")
        if c == 'y':
            start()
        else:
            print("Good Bye")

start()