print("------NESTED IF STATEMENT------")      #Nested if statement is used to check multiple conditions within another if statement.
class_attendance = float(input("Enter today's class attendance percentage: "))      # Take input from the user and convert it to an integer.
if class_attendance >= 50.0:        # Check if attendance is greater than or equal to 50.
    print("Teacher can take the class.")

    # We use an if-else chain inside to decide the syllabus outcome
    if class_attendance >= 60.0:    # Check if attendance is greater than or equal to 60.
        print("Teacher will be able to finish the syllabus.")
    else:                       # Execute if the condition in the nested if statement is false.
        print("Teacher will not be able to finish the syllabus due to lack of attendance.")

else:                       # Execute if the condition in the outer if statement is false.
    # This handles everything below 50
    if class_attendance <= 30.0:    # Check if attendance is less than or equal to 30.
        print("Principal will get to know that students are bunking the class.")
    else:                       # Execute if the condition in the nested if statement is false.
        print("Teacher cannot take the class and will not be able to finish the syllabus due to lack of attendance.")
