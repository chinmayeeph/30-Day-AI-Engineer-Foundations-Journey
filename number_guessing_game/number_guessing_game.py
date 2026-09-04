import random

maximum_number = 100

# 1. Ask user for difficulty first
difficulty = input("Choose difficulty level (EASY/MEDIUM/HARD): ")

if difficulty == "EASY":
    maximum_number = 10
    maximum_attempts = 5
elif difficulty == "MEDIUM":
    maximum_number = 50
    maximum_attempts = 7
elif difficulty == "HARD":
    maximum_number = 100
    maximum_attempts = 10
else:
    # Fallback default case in case they type something else
    maximum_number = 100
    maximum_attempts = 10

# 2. Pick the secret number AFTER maximum_number is set by difficulty
secret_number = random.randint(1, maximum_number)

# Initialize scoring variables
score = 100

# 3. Dynamic loop based on maximum_attempts
for attempt in range(1, maximum_attempts + 1):
    # Calculate the score for this attempt
    score = 100 - ((attempt - 1) * 20)

    print(f"Attempt {attempt} of {maximum_attempts}")
    print(f"Current score: {score}")

    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("TOO HIGH!!")
    elif guess < secret_number:
        print("TOO LOW!!")
    else:
        print("CORRECT!!")
        print(f"Your final score is: {score}") 
        break

