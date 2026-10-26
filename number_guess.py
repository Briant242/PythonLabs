import random

def number_guess():

    number = random.randint(1, 100)
    user_attempt = 0

    while True:
        user_guess = int(input("Guess the number (1-100): "))
        user_attempt += 1

        if user_guess < number:
            print("Your number still to low!")
        elif user_guess > number:
            print("Your number was to high!")
        elif user_guess == number:
            print(f"You got it! The number was {number}, and you get it on your {user_attempt} attempts!")
            break

print("Welcome to Number Guess CLI Minigame by Jeryco Fabriant(Briant242)!")
number_guess()