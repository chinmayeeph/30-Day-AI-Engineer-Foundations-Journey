# Problem
# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.
# 
# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.
# 
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
# 
# Hints
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split.
# Note that you can handle two exceptions separately with code like:
# try:
#     ...
# except ValueError:
#     ...
# except ZeroDivisionError:
#     ...
# Or you can handle two exceptions together with code like:
# 
# try:
#     ...
# except (ValueError, ZeroDivisionError):
#     ... 




def main():
    while True:
        fraction = input("Fraction: ")
        try:
            # Split the input string at the slash
            x_str, y_str = fraction.split("/")
            
            # Convert both components to integers
            x = int(x_str)
            y = int(y_str)
            
            # Ensure the fraction is valid (X cannot be greater than Y)
            # If Y is 0, division by zero will be caught by ZeroDivisionError
            if x > y:
                continue
                
            # Calculate and round the percentage to the nearest integer
            percentage = round((x / y) * 100)
            break
            
        except (ValueError, ZeroDivisionError):
            # If a value isn't an integer or y is 0, silently ignore and loop again
            pass

    # Print the gauge status based on the percentage
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

if __name__ == "__main__":
    main()

