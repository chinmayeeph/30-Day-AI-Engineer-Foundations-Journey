# 1. Ask the user for an input number
number = int(input("Enter a number: "))

# Handle the edge case where the number itself is 0 (which has 1 digit)
if number == 0:
    count = 1
else:
    count = 0
    # Make a copy of the number so we don't destroy the original value
    temp = abs(number)  # abs() handles negative numbers safely
    
    # 2. Loop to repeatedly remove one digit
    while temp > 0:
        temp = temp // 10  # This removes the last digit
        count += 1         # Increment the digit count

# 3. Print the final result
print(f"Number of digits = {count}")



# or
number = int(input("Enter a number: "))

# Convert to string and find its length
count = len(str(abs(number))) 

print(f"Number of digits = {count}")
