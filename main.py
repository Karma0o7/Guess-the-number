# Modules
import random


def main():
    number = random.randint(1,10)
    for i in range(0,5):
        print(f"You have {5-i} guesses left.")
        guess = int(input("Guess a number between 1-10: "))
        if(guess == number):
            print("Hurray!!")
            print(f"you guessed the number right it's {number}")
            break
        elif (guess < number):
            print("Nope, Guess Higher")
        else:
            print("Nope, Guess Lower")
    print("Thanks for playing.")


if __name__ == "__main__":
    main()