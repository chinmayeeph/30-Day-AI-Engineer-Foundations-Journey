# A for loop iterates over each item in a sequence.
# (start, stop, step) - The range function generates a sequence of numbers from start to stop in steps of step.

for x in range(10, 0, -3):   # The range function generates a sequence of numbers from 10 to 1 in steps of 3.
    print(x)                 # Print the current value of x.

age = input("Enter your age: ")  # Take input from the user and store it in the variable 'age'.
for number in range(0, 1):       # Iterate over the indices from 0 to 1 (exclusive).
    print(age[number])           # Print the character at the current index.


name = input("Enter your name: ")    # Take input from the user and store it in the variable 'name'.
for letter in range(1, len(name)):   # Iterate over the indices from 1 to the length of the name (exclusive).
    print(name[letter])              # Print the character at the current index.









