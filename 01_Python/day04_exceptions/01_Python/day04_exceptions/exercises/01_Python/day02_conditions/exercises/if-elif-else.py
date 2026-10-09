print("------IF ELIF ELSE STATEMENT------")      #elif statement is used to check multiple conditions.
marks = int(input("Enter your marks: "))      # Take input from the user and convert it to an integer.
if marks >= 90:        # Check if marks are greater than or equal to 90.
    print("You got an A grade.")
elif marks >= 80:      # Check if marks are greater than or equal to 80.
    print("You got a B grade.")
elif marks >= 70:      # Check if marks are greater than or equal to 70
    print("You got a C grade.")
else:                   # Execute if none of the above conditions are true.
    print("You need to work harder.")