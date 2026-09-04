print("-----Exercise 3 — Largest of Two Numbers-----")      # This program checks which of the two numbers is larger.
number_1 = float(input("Enter the first number: "))      # Take input from the user and convert it to a float.
number_2 = float(input("Enter the second number: "))      # Take input from the user and convert it to a float.
if number_1 > number_2:        # Check if the first number is greater than the second number.
    print("The first number is larger.")      # Print that the first number is larger.
elif number_1 < number_2:                       # Execute if the condition in the if statement is false.
    print("The second number is larger.")      # Print that the second number is larger.
else:                                   # Execute if the condition in the if statement is false.
    print("Both numbers are equal.")          # Print that both numbers are equal.