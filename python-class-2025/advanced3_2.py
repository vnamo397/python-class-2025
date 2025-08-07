import random

# Allow user to choose the range
use_custom_range = input("Do you want to choose the range? (y/n): ").lower() == 'y'
if use_custom_range:
    low = int(input("Enter the lowest number in the range: "))
    high = int(input("Enter the highest number in the range: "))
else:
    low = 1
    high = 20

secret = random.randint(low, high)
previous_guesses = []

for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt}/5 – Guess the number: "))
    previous_guesses.append(guess)
    if guess == secret:
        print("Correct! You win.")
        print(f"Your guesses: {previous_guesses}")
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")
else:
    print(f"Sorry, you’ve used all attempts. The number was: {secret}")
    print(f"Your guesses: {previous_guesses}")
