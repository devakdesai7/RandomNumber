import random

def take_input():
    guess = input()
    guess = int(guess)
    return guess

number = random.randint(1, 30)
count = 0

print("I am thinking of a number between 1 and 2z0.")
print("Take a guess.")

guess = take_input()

while True:
    if (guess == number):
        count += 1
        print(f"Good job, you guessed the number correctly in {count} guesses")
        break
    elif (guess < number):
        count += 1
        print("Your guess is too low")
        print("Take a guess")
        guess = take_input()
    elif(guess > number):
        count += 1
        print("Your guess is too high")
        print("Take a guess")
        guess = take_input()