number = int(input("Enter a number: "))

reversed_number = 0
temp = number

while temp != 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp //= 10

print(f"Reverse number: {reversed_number}")