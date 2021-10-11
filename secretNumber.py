import random
secret = random.randint(1, 20)

while True:
    guess = int(input("Guess the secret number (between 1 and 20): "))

    if guess == secret:
        print(f"Congratulations, you've guessed it! It's number '{secret}'")
        break
    elif guess > secret:
        print("Your guessed number is not correct. The correct number is SMALLER.")
    elif guess < secret:
        print("Your guessed number is not correct. The correct number is BIGGER.")
