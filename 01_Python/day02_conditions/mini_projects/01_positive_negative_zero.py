print("-----Exercise 1 — Positive / Negative / Zero-----")      # This program checks if a number is positive, negative, or zero.
number = float(input("Enter a number: "))      # Take input from the user and convert it to a float.
if number > 0:        # Check if the number is greater than 0.
    print("The number is positive.")      # Print that the number is positive.
elif number < 0:                       # Execute if the condition in the if statement is false.
    print("The number is negative.")      # Print that the number is negative.
else:                                   # Execute if the condition in the if statement is false.
    print("The number is zero.")          # Print that the number is zero.