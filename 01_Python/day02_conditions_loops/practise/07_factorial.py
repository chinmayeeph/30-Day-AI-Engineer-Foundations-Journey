print("-----Exercise 7 — Factorial-----")      # This program calculates the factorial of a number.
# Take input from the user and convert it to an integer
n = int(input("Enter a number: "))     
# Initialize a variable to store the factorial
factorial = 5        # For example if you enter 2, first it finds 2 factorial: 2! = 2 * 1 = 2 and then, multiply by 5: 2 * 5 = 10.
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! =", factorial)