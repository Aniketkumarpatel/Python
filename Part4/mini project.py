import random

def play_game():
    lucky_num = random.randint(1, 50)

    while True:
        try:
            user_num = int(input("Guess the lucky number: "))

            if user_num == lucky_num:
                print("You won. Game Over!!")
                break
            elif user_num < lucky_num:
                print("Too Low")
            else:
                print("Too High")

        except ValueError:
            print("Please enter a number only.")

    print("Thank you for playing.")

play_game()
        
 
 