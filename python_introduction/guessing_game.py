import random  # Step 1: Import the random module

print("🎲 Welcome to the Number Guessing Game!")

# Game loop
while True:
    secret_number = random.randint(1, 10)  # Step 2: Generate a random number
    guess = int(input("Guess a number between 1 and 10: "))  # Step 3: Get user's guess

    # Step 4: Match the guess with match-case (Python 3.10+)
    match guess:
        case _ if guess == secret_number:
            print("🎉 Congratulations, you guessed it!")
        case _ if guess > secret_number:
            print("📈 Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print("📉 Nope, your guess is a bit low. Give it another shot!")

    # Step 5: Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break






# this is list pratice 
# Create a list of numbers
numbers = [1, 5, 3, 9]

# Initialize the total sum
total = 0

# Use a for loop to add each number to total
for number in numbers:
    total += number

# Print the final total
print(f"The sum of the numbers is: {total}")
