import random
import time

def clap_animation():
    for _ in range(5):
        print("👏", end=" ")
        time.sleep(0.5)
    print("Ramesh Salaria is genius")

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Well done! You guessed the number in {attempts} attempts.")
            print(f"Time taken: {elapsed_time:.2f} seconds")
            clap_animation()
            break

guessing_game()
