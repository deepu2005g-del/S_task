# Task 2: Guess the Number Game

import random

def guess_game():
    try:
        number = random.randint(1, 100)
        attempts = 0

        print("Guess the number between 1 and 100!")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < 1 or guess > 100:
                    raise ValueError("Number must be between 1 and 100")

                if guess < number:
                    print("The value is lower than the expected one!")
                elif guess > number:
                    print("The value is higher than the expected one!")
                else:
                    print(f"Correct! You guessed in {attempts} attempts.")
                    break

            except ValueError:
                print("Invalid input! Enter a number between 1 and 100.")
            except Exception as e:
                print("Error:", e)

    except Exception as e:
        print("Game Error:", e)

if __name__ == "__main__":
    guess_game()