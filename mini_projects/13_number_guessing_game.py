import random

replay = "yes"

while replay == "yes":
    maximum_number = 100
    maximum_attempts = 10
    
    # 1. Get difficulty choice
    difficulty = input("Choose difficulty level (EASY/MEDIUM/HARD): ").upper().strip()

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
        difficulty = "HARD (DEFAULT)"
        maximum_number = 100
        maximum_attempts = 10

    print(f"Difficulty set to: {difficulty}")

    # 2. Setup the secret number and game state
    secret_number = random.randint(1, maximum_number)
    attempt = 1
    game_won = False

    # 3. Game loop for guessing
    while attempt <= maximum_attempts:
        # Calculate score
        score = 100 - ((attempt - 1) * 10)
        if score < 0:
            score = 0

        print(f"\nAttempt {attempt} of {maximum_attempts}")
        print(f"Current score: {score}")

        # Get user guess safely
        user_input = input("Guess the number: ").strip()
        if not user_input.isdigit():
            print("Please enter a valid number!")
            continue
            
        guess = int(user_input)

        # Check the guess
        if guess > secret_number:
            print("TOO HIGH!!")
            attempt = attempt + 1
        elif guess < secret_number:
            print("TOO LOW!!")
            attempt = attempt + 1
        else:
            print("CORRECT!!")
            print(f"Your final score is: {score}")
            game_won = True
            break

    # If they ran out of attempts and didn't win
    if not game_won:
        print(f"\nGame Over! You ran out of attempts. The number was {secret_number}.")

    # 4. Ask to play again
    print("")
    replay = input("Play again? (Yes/No): ").strip().lower()

print("Goodbye!")