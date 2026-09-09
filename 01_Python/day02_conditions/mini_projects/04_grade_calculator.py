print("-----Exercise 4 — Grade Calculator-----")      # This program calculates the grade based on the marks obtained.

# Take input from the user and convert to float
marks = float(input("Enter the marks obtained: "))

# Use if-elif-else to check conditions mutually exclusively
if marks >= 90:
    print("Grade: A+ \nRemarks: Excellent")
elif marks >= 80:
    print("Grade: A \nRemarks: Good")
elif marks >= 70:
    print("Grade: B+ \nRemarks: Satisfactory")
elif marks >= 60:
    print("Grade: B \nRemarks: Fair")
elif marks >= 50:
    print("Grade: C+\nRemarks: Needs Improvement")
elif marks >= 40:
    print("Grade: C \nRemarks: Poor")
elif marks >= 30:
    print("Grade: D \nRemarks: Very Poor")
else:
    print("Grade: F \nRemarks: Fail")